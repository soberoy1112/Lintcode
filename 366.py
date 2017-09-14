#/usr/bin/env python3
# -*- coding: utf-8 -*-
L = [0, 1]
n = int(input('give a number:'))
for i in range(3, n + 1):
	L.append(L[i - 3] + L[i - 2])
print(L)
x = int(input('Which number do you want? '))
if x < 11:
	print(L[x - 1])
else:
	print('you are out of range!')