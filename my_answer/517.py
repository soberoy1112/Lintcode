#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):

    def __init__(self, n):
        self.n = n

    def isUgly(self):
        if self.n == 0:
            return 1
        else:
            while self.n % 2 == 0:
                self.n = self.n // 2
            while self.n % 3 == 0:
                self.n = self.n // 3
            while self.n % 5 == 0:
                self.n = self.n // 5
            return self.n
x = int(input('Please give a number: '))
y = Solution(x)
if y.isUgly() == 1:
    print('True')
else:
    print('False')