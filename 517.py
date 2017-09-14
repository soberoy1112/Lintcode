#/usr/bin/env python3
# -*- coding: utf-8 -*-
strr = 'abcdefghijklmnopqrstuvwxyz'
L = list(strr)
n = 0
flag = 0
for i in L:
	n += 1
	L.pop(n - 1)
	if i in L:
		flag = 1
		break
	L.insert(n - 1, i)
if flag == 1:
	print('False')
elif flag == 0:
	print('True')