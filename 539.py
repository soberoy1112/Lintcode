#/usr/bin/env python3
# -*- coding: utf-8 -*-
nums = [0, 1, 0, 3, 12]
for i in range(0, len(nums)):
	if nums[i] == 0:
		nums.pop(i)
		nums.append(0)
print(nums)