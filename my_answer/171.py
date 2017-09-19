#/usr/bin/env python3
# -*- coding: utf-8 -*-
L = ["lint","intl","inlt","code"]
LL = []
a = 'lint'
b = 'intl'
A = list(a)
B = list(b)
def lengthEqual(x, y):
	if len(x) == len(y):
		return True
	else:
		return False
print(lengthEqual(A, B))
def wordEqual(m, n):
	flag = 1
	x = list(m)
	y = list(n)
	for i in x:
		if i in y:
			for j in range(len(y)):
				if i == y[j]:
					y[j] = '0'
					break
		else:
			flag = 0
			return False
	if flag == 1:
		return True
print(wordEqual(A, B))
for i in range(len(L)):
	for j in range(i + 1, len(L)):
		if lengthEqual(L[i], L[j]) and wordEqual(L[i], L[j]):
			LL.append(L[i])
print(LL)


