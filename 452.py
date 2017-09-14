#/usr/bin/env python3
# -*- coding: utf-8 -*-
str = '1->2->3->3->4->5->3'
strr = ''
for i in str:
	if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
		print(i)
		strr = strr + i + '->'
print(strr[:-2])