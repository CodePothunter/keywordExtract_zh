# -*- coding: utf8 -*-
from getKeytag import terminology

if __name__ == '__main__':
	terms = terminology("example.txt")
	for word in terms:
		print word.encode('gbk','ignore')