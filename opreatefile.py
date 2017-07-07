#!/usr/bin/env python
# coding: UTF-8 
import codecs
f = codecs.open('file_ch.txt','w','utf-8')

f.write(u'你好！\n')
f.write(u'很高兴见到你\n')
f.close()

f = codecs.open('file_ch.txt','r','utf-8')
print f.read(2)
print f.readline()
print f.readline()
print f.read(2)