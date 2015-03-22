# -*- coding:utf8 -*-

# import jieba.analyse as textrank
import kwExtract

def loadFile(filename):
	"""
		输入文件名读取文件中内容。
	"""
	f = open(filename, 'r')
	article = []
	for line in f.readlines():
		article.append(line.decode('gbk','ignore'))
	f.close()
	return article


def tag_extract(text, topK = 2, span = 3):
	"""
		text 为正文，string类型
		topK 表示这一段文字最多产生topK个关键词
		span 表示输出的关键术语至少是几个字，建议设置4个字。
	"""
	
	keyWords = kwExtract.extract_tags(text, withWeight=True, span = span)
	return keyWords[:topK]

def terminology(filename, topK = 10):
	"""
		输出不多于topK个由该文件产生的术语。
	"""
	content = loadFile(filename)
	term = []
	for c in content:
		term += tag_extract(c, span = 4)
	term.sort(key = lambda x:x[1])
	res = []
	for w in term:
		res += [w[0]]
	res = list(set(res))[:topK]
	return res



if __name__ == '__main__':
	#示例文件是生物进化课的课程讲义。
	terms = terminology("example.txt")
	for word in terms:
		print word.encode('gbk','ignore')