class Solution:
    """
    @param: num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):
        # write your code here
        while num > 9:
            s = 0 
            for i in str(num):
                s = s + int(i)
            num = s
        return num

x = Solution()
print(x.addDigits(38))