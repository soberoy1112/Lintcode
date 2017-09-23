class Solution:

	def isUgly(self, num):
		if num <= 0:
			return False
		elif num == 1:
			return True
		elif num >= 2:
			while num % 2 == 0:
				num /= 2
			while num % 3 == 0:
				num /= 3
			while num % 5 == 0:
				num /= 5
		if num == 1:
			return True
		else:
			return False
x = int(input("Input an integer: "))
y = Solution()
print(y.isUgly(x))