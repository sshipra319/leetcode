def height(root):
    if not root:
        return -1
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    if left_height > right_height:
        return left_height + 1
    
    else:
        return right_height + 1