def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if root.val < val:
                root.right = self.insertIntoBST(root.right, val)
            else:
                root.left = self.insertIntoBST(root.left, val)
    
        return root