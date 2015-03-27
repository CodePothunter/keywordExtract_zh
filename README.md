# keywordExtract_zh

<h1>中文关键术语提取工具<br/></h1>
A Chinese key terminology extraction tool for MOOC.<br/>
本工具需要依赖jieba最新版分词。<br/>

使用时将文件夹放到目录下，强此文件夹作为整个包导入即可。

目前仅有terminology函数可用。
###使用示例
	from keywordExtract_zh import terminology

	if __name__ == '__main__':
		terms = terminology("example.txt")
			for word in terms:
				print word.encode('gbk','ignore')
###
