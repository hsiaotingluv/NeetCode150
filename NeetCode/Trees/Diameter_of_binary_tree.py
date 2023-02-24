# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = []
        self.dfs(root, res)
        return max(res)

    def dfs(self, root, res):
        if not root:
            return 0
        
        left_height = self.dfs(root.left, res)
        right_height = self.dfs(root.right, res)

        res.append(left_height+right_height)

        return max(left_height, right_height)+1
    '''
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        currMax = self.maxDepth(root.left) + self.maxDepth(root.right)
        leftMax = self.diameterOfBinaryTree(root.left)
        rightMax = self.diameterOfBinaryTree(root.right)
        return max(currMax, leftMax, rightMax)
        
    
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root: 
            return 0
        
        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepth(root.right)

        return max(maxLeft, maxRight) + 1





