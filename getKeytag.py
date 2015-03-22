# -*- coding:utf8 -*-

# import jieba.analyse as textrank
import kwExtract

def loadFile(filename):
	f = open(filename, 'r')
	article = []
	for line in f.readlines():
		article.append(line.decode('gbk','ignore'))
	f.close()
	return article


def tag_extract(text, topK = 2, stopWords = None):
	keyWords = kwExtract.extract_tags(text, withWeight=False)
	return keyWords[:topK]

def terminology(filename, topK = 2):
	content = loadFile(filename)
	term = []
	for c in content:
		term += tag_extract(c)
	term = set(term)
	return list(term)


if __name__ == '__main__':
	terms = terminology("example.txt")
	for word in terms:
		print word.encode('gbk','ignore')