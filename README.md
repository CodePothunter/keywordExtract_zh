# keywordExtract_zh

<h1>中文关键术语提取工具<br/>A Chinese key terminology extraction tool for MOOC.<br/></h1>

本工具需要依赖jieba最新版分词。<br/>

使用时将整个文件夹放到工作目录下，作为工具包调用。

目前仅有terminology函数可用。
###使用示例
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

<h2>功能说明</h2>
使用jieba的tf-idf的方法提取关键词，去除停用词，同时根据术语出现在语料库中频率小的特点，过滤掉本身idf值较低的词语，因为这些词语是常见词，不太可能成为术语。此外，还利用了jieba分词工具中的词性标注功能，只允许部分词性的词语作为关术语。<br/>

停用词表是一个需要维护的规则表，里面是对话或者文章中高频出现却没有特殊涵义的词语。<br/>

terminology提供了5个参数，第一个是文章源，topK表示输出（最多）多少个术语,span表示术语最少有多少个字,threshold是常见词过滤阈值 i.e. 如果一个词idf值较低则认为它是术语的可能性较低,mode表示文件的读取模式，1表示分段读取和处理，最终汇总统计；2表示全文同时统计。<br/>

默认为topK = 10, span = 2, threshold = 5, mode = 1。<br/>
