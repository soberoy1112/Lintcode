#/usr/bin/env python3
# -*- coding: utf-8 -*-
L = [3, 2, 1, 4, 6, 5, 3, 23, 4, -3, 0, 2, -11, 8]
for i in range(len(L) - 1):
	for j in range(len(L) - 1 - i):
		if L[j] > L[j + 1]:
			L[j], L[j + 1] = L[j + 1], L[j]
print(L)

