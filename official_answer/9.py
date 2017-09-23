class Solution:
    """
    @param: n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        l = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                l.append("fizz buzz")
            elif i % 5 == 0:
                l.append("buzz")
            elif i % 3 == 0:
                l.append("fizz")
            else:
                l.append(str(i))
        return l

L = Solution()
print(L.fizzBuzz(15))
