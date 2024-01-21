# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(current) :
            if not current.left and not current.right :
                return 1

            a = 0
            b = 0
            if current.left :
                a = dfs(current.left)
            if current.right :
                b = dfs(current.right)
            return a + 1 if a > b else b + 1
        
        if not root : return 0
        return dfs(root)