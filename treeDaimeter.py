def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        
        def depthTree(node):
            if node is None:
                return 0
            left = depthTree(node.left)
            right = depthTree(node.right)
            self.ans = max(self.ans, left+right+1)
            return max(left, right)+1
        
        depthTree(root)
        return self.ans-1