class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        # write your code here
        s = ""
        flag = True
        if str == "":
            return True
        for i in range(len(str)):
            s = str[:i] + str[i + 1:]
            for j in s:
                if str[i] in s:
                    return False
        return flag
x = Solution()
print(x.isUnique("aabc"))

