# -*- coding: utf8 -*-
from getKeytag import terminology

if __name__ == '__main__':
	#example.txt是生物进化课的课程讲义。
	#example2.txt经济学思想史讲义
	terms = terminology("example2.txt", topK = 10, span = 2, threshold = 5, mode = 1)
	#topK表示输出（最多）多少个术语
	#span表示术语最少有多少个字
	#threshold是常见词过滤阈值 i.e. 如果一个词idf值较低则认为它是术语的可能性较低
	#mode表示文件的读取模式，1表示分段读取和处理，最终汇总统计；2表示全文同时统计；
	for word in terms:
		print word.encode('gbk','ignore') #此处的编码需要根据运行环境做修改
