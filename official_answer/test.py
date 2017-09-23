class Solution:
    """
    @param: nums: an integer array
    @return:
    """
    def moveZeroes(self, nums):
        # write your code here
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1