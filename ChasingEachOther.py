# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:54:27 2020

@author: Shipra
"""

nums = [0, 1, 0, 3, 0, 12]

class Solution:
    def MoveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        return nums

sol = Solution()
print(sol.MoveZeroes(nums))