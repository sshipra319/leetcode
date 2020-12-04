

def lexSmallest(a): 
   a.sort()
   n = len(a)
   answer = "" 
   for i in range(n): 
       answer += a[i] 
 
   return answer 

#a = ['c', 'cc', 'cca', 'cccb']
a = ['abc', 'ab', 'bc']
print(lexSmallest(a))

