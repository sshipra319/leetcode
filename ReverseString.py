# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:39:41 2020

@author: Shipra
"""

arr = ["h", "e", "l", "l", "o"]
 
class Solution:
    
    def ReverseString(self, arr):
        l = 0
        r = len(arr) - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr

sol = Solution()
print(sol.ReverseString(arr))
        
            

