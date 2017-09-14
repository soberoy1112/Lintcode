#/usr/bin/env python3
# -*- coding: utf-8 -*-
class checkNum(object):
	def __init__(self, num):
		self.num = num
	def isUgly(self):
		if self.num == 0:
			return 1
		else:
			while self.num%2 ==0:
				self.num = self.num // 2
			while self.num%3 ==0:
				self.num = self.num // 3
			while self.num%5 ==0:
				self.num = self.num // 5
			return self.num
x = int(input('Please give a number: '))
n = checkNum(x)
if n.isUgly() == 1:
	print('True')
else:
	print('False')