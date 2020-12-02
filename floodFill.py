def floodFill(image, sr, sc, newColor):
  R = len(image)
  L = len(image[0])
  color = image[sr][sc]
  if color == newColor:
    return image
  
  def dfs(r, c):
    if image[r][c] == color:
      image[r][c] = newColor
      if r >= 1:
        dfs(r-1, c)
      if r+1 < R:
        dfs(r+1, c)
      if c >= 1:
        dfs(r, c-1)
      if c+1 < L:
        dfs(r, c+1)
        
  dfs(sr, sc)
  return image
  
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
result = floodFill(image, sr, sc, newColor)
print(result)