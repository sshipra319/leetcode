# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 13:50:47 2020

@author: Shipra
"""

arr = [-1, 0, 1, 2, -1, -4]

class Solution:
    
    def threeSum(self, arr):
        lst = set()
        arr.sort()
        for i in range(0, len(arr)-1):
            first = i            
            left = i + 1
            right = len(arr) - 1            
            while left < right:
                target = arr[first] + arr[left] + arr[right]
                if target == 0:
                    lst.add(tuple([arr[first], arr[left], arr[right]]))
                    #return[tuple([arr[first], arr[left], arr[right]])]
                    left += 1
                    right -= 1
                elif target > 0:
                    right -= 1                    
                else:
                    left += 1                   
        return lst
  
sol = Solution()
print(sol.threeSum(arr))
