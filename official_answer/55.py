class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: if A contains all of the characters in B return true else false
    """
    def compareStrings(self, A, B):
        # write your code here
        flag = True
        if B == "":
            flag = True
        else:
            if len(B) > len(A):
                flag = False
                return flag
            else:
                for i in B:
                    if i not in A:
                        flag = False
                        return flag
                    else:
                        A = A.replace(i, "0", 1)
                        print(i)
                        print(A)
        return flag
x = Solution()
print(x.compareStrings("ABCDEFG", "ACC"))