#/usr/bin/env python3
# -*- coding: utf-8 -*-
strr = '1->2->3->4->5->6->7'
L = []
LL = []
LLL = []
LLLL = []
counter = 0
for i in strr:
	if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
		counter += 1
		L.append(int(i))
for j in range(0, len(L)):
	if j%2 == 1:
		LL.append(L[j - 1])
		LL.append(L[j])
		LLL = LL
		LL = []
		LLL.reverse()
		LLLL.append(LLL[0])
		LLLL.append(LLL[1])
		print(LLL)
if len(L)%2 == 1:
	LLLL.append(L[-1])
print(LLLL)
