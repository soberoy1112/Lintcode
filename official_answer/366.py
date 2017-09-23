class Solution:
    """
    @param: n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        l = [0, 1]
        if n <= 0:
            return False
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            for i in range(3, n + 1):
                l.append(l[i - 3] + l[i - 2])
            return l[n - 1]

L = Solution()
print(L.fibonacci(10))