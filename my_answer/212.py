#/usr/bin/env python3
# -*- coding: utf-8 -*-
strr = "Mr John Smith"
L = strr.split()
strrr = ''
for i in L:
	strrr = strrr + i + "%20"
print(strrr[:-3])
print(len(strrr[:-3]))