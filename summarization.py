# -*- coding:utf8 -*-

import jieba.posseg as pseg

modalParticleList = [u"吗",u"吧",u"呢",u"啊",u"呀",u"哎",u"唉", u"哼", u"呐", u"哇"]
pronounList = [u"什么",u"为什么", u"怎么", u"怎么样", u"如何", u"多么", u"哪里", u"哪儿", u"凭什么", u"难道", ]

class Sentences:
    def __init__(self, pPosi, cPosi, content):
        self.mood = 0 #语气设定：1 陈述句 0 非陈述句
        self.content = content
        self.isKeySent = 0 #0 不是关键句子 1 是关键句子
        self.weight = 0;
        self.paraPosi = pPosi; #表示句子在文段中的位置
        self.contPosi = cPosi
        self.words = list(pseg.cut(content))
    def analyzeMood(self):
        if self.content == "":
            return False
        flag = True
        for w in self.words:
            if(w.flag == "y" and w.word in modalParticleList) or (w.flag == 'r' and w.word in pronounList):
                flag = False
        self.mood = flag
        return flag
    def calcWeight(self,keywords):
        # words = pseg.cut(self.content)
        for w in self.words:
            if(w.word in keywords):
                # print w.word.encode('gbk','ignore')
                self.weight += 1
        if(self.paraPosi == 0):
            self.weight *= 1.2
        # print self.weight
        return self.weight



def summarGener(content, keywords, length = 10):
    numOfWeight = []
    sentSet = []
    res = []
    if(type(content)==type(str)):
        content = [content]
    for j in range(len(content)):
        para = content[j]
        sents = para.split(u'。');
        for i in range(len(sents)):
            if(sents[i].strip() == ""):
                continue
            else:
                sents[i]+=u'。'
            sentence = Sentences(i,j,sents[i])
            if(sentence.analyzeMood()):
                w = (sentence.calcWeight(keywords))
                numOfWeight.append(w)
                sentSet.append(sentence)
    numOfWeight.sort(reverse = True)
    if len(numOfWeight) < length:
        return [content]
    else:
        threshold = numOfWeight[length-1]
        for sentence in sentSet:
            if sentence.weight >= threshold:
                res.append(sentence.content)
        return res




