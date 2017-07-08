#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-08
# @Author  : Maobi Zhu (zhumaobi@qq.com)
# @Link    : https://github.com/zhumaobi/pyhtonLearning

import re, os
try:
	fp = open("email.txt",'r')
except:
	print "文件打开失败"

string = fp.readlines()
fp.close()

fp = open("re_reslt.txt",'w')
for my_str in string:
    data = re.findall(r'(\w+)@(\w+)(\.\w+)', my_str)
#    print data
    for resl in data:
        for i in xrange(len(resl)):
        	if i == len(resl)-1:
        		fp.write(resl[i] + '\n')
        	else:
        		fp.write(resl[i] + ' ')
            
fp.close()