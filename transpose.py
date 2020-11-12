def transpose(A):
  trans = []
  rows = len(A)
  cols = len(A[0])
  for i in range(rows):
    temp = []
    for j in range(cols):
      temp.append(A[j][i])    
      
    trans.append(temp)
  
  return trans
  
A = [[1,2,3],[4,5,6],[7,8,9]]
result = transpose(A)
print(result)
