def shuffleString(s, indices):
  shuffle = list(s)
  l = len(s)
  for i in range(l):
    shuffle[indices[i]] = s[i]
  return "".join(shuffle)
  

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
sh = shuffleString(s, indices)
print(sh)