class Solution:
    """
    @param: A: an integer array
    @return: 
    """
    def sortIntegers(self, A):
        # write your code here
        for i in range(len(A)):
            for j in range(len(A) - 1):
                if A[i] < A[j]:
                    A[i], A[j] = A[j], A[i]
        return A
            

x = Solution()
print(x.sortIntegers([3, 2, 1, 4, 5]))

