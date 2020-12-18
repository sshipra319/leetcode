# -*- coding: utf-8 -*-
"""
@author: Shipra
"""

num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 5, 6]
m = 3
n = 3

class Solution:
    def mergeArray(self, num1, num2, m, n):
        i, j = 0, 0
        num3 = []
        while i < m and j < n:
            if num1[i] < num2[j]:
                num3.append(num1[i])
                i += 1
            elif num1[i] > num2[j]:
                num3.append(num2[j])
                j += 1
            else:
                num3.append(num1[i])
                i += 1
                num3.append(num2[j])
                j += 1
        
        while i < m:
            num3.append(num1[i])
            i += 1
        
        while j < n:
            num3.append(num2[j])
            j += 1
        
        for x in range(0, len(num3)):
            num1[x] = num3[x]
            
        return num1
        
        
sol = Solution()
print(sol.mergeArray(num1, num2, m, n))
