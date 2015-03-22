# keywordExtract_zh

中文关键术语提取工具
A Chinese key terminology extraction tool for MOOC.
本工具需要依赖jieba最新版分词。

使用时将文件夹放到目录下，然后from keywordExtract_zh import terminology

目前仅有terminology函数可用

if __name__ == '__main__':
	terms = terminology("example.txt")
	for word in terms:
		print word.encode('gbk','ignore')
