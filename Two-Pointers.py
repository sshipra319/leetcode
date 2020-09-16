# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:50:08 2020

@author: Shipra
"""

arr = [2, 7, 11, 15]
target = 9

class Solution:
    def Sum(self, arr, target):
        l = 0
        r = len(arr) - 1
        
        while l < r:
            sum = arr[l] + arr[r]
            
            if sum == target:
                return [l, r]
            elif sum < target:
                l += 1
            else:
                r -= 1
    
        return[-1, -1]
    
            
sol = Solution()
print(sol.Sum(arr, target))
