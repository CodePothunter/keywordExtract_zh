# -*- coding:utf8 -*-

# import jieba.analyse as textrank
import kwExtract

def loadFile(filename, mode = 1):
	"""
		输入文件名读取文件中内容。
	"""
	f = open(filename, 'r')
	if mode ==1:
		article = []
		for line in f.readlines():
			article.append(line.decode('gbk','ignore'))
	elif mode == 2:
		article = ""
		for line in f.readlines():
			article+=(line.strip().decode('gbk','ignore'))
	else:
		print "WRONG MODE CHOOSE"
		articl = ""
	f.close()
	print "Article Loading Complete..."
	return article


def tag_extract(text, withWeight=True, topK = 10, span = 2, threshold = 10):
	"""
		text 为正文，string类型
		topK 表示这一段文字最多产生topK个关键词
		span 表示输出的关键术语至少是几个字。
		threshold 表示已出现在idf词表中的词语的idf阈值是多大
	"""
	
	keyWords = kwExtract.extract_tags(text, withWeight=withWeight, span = span, threshold = threshold)
	return keyWords[:topK]

def terminology(filename, topK = 10, span = 2, threshold = 5, mode = 1):
	"""
		输出不多于topK个由该文件产生的术语。
		mode: 如果mode值为1则采用分段统计的方法；如果mode值为2则将整篇讲义合成一篇文章进行提取
	"""
	content = loadFile(filename, mode = mode)
	if mode == 1:
		term = {}
		num = 0.0
		for c in content:
			new_term = tag_extract(c, topK = topK, span = 2, threshold = threshold)
			for item in new_term:
				term[item[0]] = term.get(item[0],0.0)+item[1]
			num += 1.0
			print "working\t%f"%(num/(len(content)+0.0)*100),"%"
		res = sorted(term, key=term.__getitem__, reverse=True)[:topK]
	elif mode == 2:
		res = tag_extract(content, withWeight = False, topK = topK, span = 2, threshold = threshold)[:topK]
	return res



if __name__ == '__main__':
	#example.txt是生物进化课的课程讲义。
	#example2.txt是经济学思想史讲义
	terms = terminology("example2.txt", topK = 10, span = 2, threshold = 5, mode = 1)
	for word in terms:
		print word.encode('gbk','ignore')