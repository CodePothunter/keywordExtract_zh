# -*- coding:utf8 -*-

import jieba.analyse


def loadFile(filename):
	f = open(filename, 'r')
	article = []
	for line in f.readlines():
		article.append(line.decode('gbk','ignore'))
	return article

def tag_extract(text, topK = 20, stop_words = None):
	tag_filter = ['an', 'i', 'j', 'l', 'n', 'nr', 'nrfg', 'ns', 'nt', 'nz', 't', 'v', 'vd', 'vn', 'eng']
	keyWords = jieba.analyse.extract_tags(text, withWeight=True)
	for word in keyWords:
		print word
		if word[1] in tag_filter:
			print word[0]

if __name__ == '__main__':
	art = loadFile("example.txt")
	for t in art:
		tag_extract(t)