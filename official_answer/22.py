class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        if isinstance(nestedList, int):
            return [nestedList]
        S = str(nestedList)
        s = ""
        flag = False
        L = []
        for i in S:
            if i == "-" or i.isdigit():
                s += i
                flag = True
            else:
                if flag is True:
                    L.append(int(s))
                    s = ""
                    flag = False
        return L

        
x = Solution()
print(x.flatten([1,2,[1,22]]))