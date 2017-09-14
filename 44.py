#/usr/bin/env python3
# -*- coding: utf-8 -*-
L = [1, 3, -11, 6, 2, 7, 9, 0, -1, 1, 3, 1, 34, 124, 22]
LL = sorted(L)
summ = 0
if LL[0] < 0:
	for i in range(0, len(LL) - 1):
		summ = summ + LL[i]
		if LL[i] >= 0:
			break
elif LL[0] >= 0:
	summ = LL[0]
print(summ)		