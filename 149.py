#/usr/bin/env python3
# -*- coding: utf-8 -*-
L =  [3,2,3,1,2,8,4]

def biggestDelta(l):
	LL = []
	D = {}
	DD = {}
	for i in range(len(l)):
		for j in range(i + 1, len(l)):
			delta = l[j] - l[i]
			LL = [i, j]
			D[str(LL)] = delta
	for (key, value) in D.items():
		if value == sorted(D.items(), key = lambda item:item[1])[-1][1]:
			DD[key] = value
	return DD
def date(x):
	if x == 0:
		return ('Monday')
	elif x == 1:
		return ('Tuesday')
	elif x == 2:
		return ('Wednesday')
	elif x == 3:
		return ('Thursday')
	elif x == 4:
		return ('Friday')
	elif x == 5:
		return ('Saturday')
	elif x == 6:
		return ('Sunday')
def main(l):
	D = biggestDelta(l)
	print('Good News! You have %d chances to get best benifit!' % len(D))
	for (key, value) in D.items():
		print('You can buy it on %s, and sale it on %s. Then you will get %d!' % (date(int(key[1])), date(int(key[4])), value))
main(L)#/usr/bin/env python3
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