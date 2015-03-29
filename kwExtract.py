#encoding=utf-8
# -*- coding: utf8 -*-
#本文件修改自结巴分词工具中的\analyse\__init__.py
import jieba
import jieba.posseg as pseg
import os
from operator import itemgetter


def loadStopWord(filename):
    f = open(filename, 'r')
    stopWords = []
    for line in f.readlines():
        try:
            stopWords.append(line.strip().decode('utf8','ignore'))
        except:
            print "DECODE ERROR\n"
    f.close()
    return stopWords

_curpath = os.path.normpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
abs_path = os.path.join(_curpath, "idf.txt")

FLAG_FILTER = ['an', 'i', 'j', 'l', 'n', 'nr', 'nrfg', 'ns', 'nt', 'nz', 't', 'v', 'vd', 'vn']
STOP_WORDS = set(loadStopWord("stopword.data"))

class IDFLoader:
    def __init__(self):
        self.path = ""
        self.idf_freq = {}
        self.median_idf = 0.0

    def set_new_path(self, new_idf_path):
        if self.path != new_idf_path:
            content = open(new_idf_path, 'rb').read().decode('utf-8')
            idf_freq = {}
            lines = content.rstrip('\n').split('\n')
            for line in lines:
                word, freq = line.split(' ')
                idf_freq[word] = float(freq)
            median_idf = sorted(idf_freq.values())[len(idf_freq)//2]
            self.idf_freq = idf_freq
            self.median_idf = median_idf
            self.path = new_idf_path

    def get_idf(self):
        return self.idf_freq, self.median_idf

idf_loader = IDFLoader()
idf_loader.set_new_path(abs_path)

def set_idf_path(idf_path):
    new_abs_path = os.path.normpath(os.path.join(os.getcwd(), idf_path))
    if not os.path.exists(new_abs_path):
        raise Exception("jieba: path does not exist: " + new_abs_path)
    idf_loader.set_new_path(new_abs_path)

def set_stop_words(stop_words_path):
    global STOP_WORDS
    abs_path = os.path.normpath(os.path.join(os.getcwd(), stop_words_path))
    if not os.path.exists(abs_path):
        raise Exception("jieba: path does not exist: " + abs_path)
    content = open(abs_path,'rb').read().decode('utf-8')
    lines = content.replace("\r", "").split('\n')
    for line in lines:
        STOP_WORDS.add(line)

def extract_tags(sentence, topK=20, withWeight=True, span = 2, threshold = 10):
    """
    Extract keywords from sentence using TF-IDF algorithm.
    Parameter:
        - topK: return how many top keywords. `None` for all possible words.
        - withWeight: if True, return a list of (word, weight);
                      if False, return a list of words.
        - span: the minimum length of a word
        - threshold: the minimum idf frequency of a word in idf.txt
    """
    global STOP_WORDS, idf_loader

    idf_freq, median_idf = idf_loader.get_idf()

    words = pseg.cut(sentence)
    freq = {}
    for w in words:
        if len(w.word.strip()) < span or w.word.lower() in STOP_WORDS or w.word in STOP_WORDS or w.flag not in FLAG_FILTER or (idf_freq.get(w.word, -1) != -1 and idf_freq.get(w.word)<threshold):
            continue
        freq[w.word] = freq.get(w.word, 0.0) + 1 #在文章中每出现一次就加1
    total = sum(freq.values())
    for k in freq:
        freq[k] *= idf_freq.get(k, median_idf) / total
    if withWeight:
        tags = sorted(freq.items(), key=itemgetter(1), reverse=True)
    else:
        tags = sorted(freq, key=freq.__getitem__, reverse=True)
    if topK:
        return tags[:topK]
    else:
        return tags
