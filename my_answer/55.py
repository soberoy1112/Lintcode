#/usr/bin/env python3
# -*- coding: utf-8 -*-
A = "ABCD"
B = "ACD"
def replaceAndCheck(x, y):
	flag = False
	L1 = list(x)
	L2 = list(y)
	for i in L2:
		if i not in L1:
			flag = False
			break
		else:
			for j in range(len(L1)):
				if i == L1[j]:
					L1[j] = '0'
					flag = True
	return flag

print(replaceAndCheck(A, B))