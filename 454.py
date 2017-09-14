#/usr/bin/env python3
# -*- coding: utf-8 -*-
class Rectangle(object):
	def __init__(self, width, height):
		self.__width = width
		self.__height = height
	def setArea(self, width, height):
		if width > 0 and height > 0:
			self.__width = width
			self.__height = height
		else:
			print('Sorry, we don\'t accept minus and zero!')
			self.__width = 0
			self.__height = 0
	def getArea(self):
		return self.__width * self.__height
area = Rectangle(1, 1)
print("""The initial square is 1 x 1.
So the area of initial square is 1.
Now, please give the width and height of your square:""")
x = int(input('The width = '))
y = int(input('The height = '))
area.setArea(x, y)
z = area.getArea()
if z > 0:
	print('The area of your square is: %d' % z)
else:
	print('')
	