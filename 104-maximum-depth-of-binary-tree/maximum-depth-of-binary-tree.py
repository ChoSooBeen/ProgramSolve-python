# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(current) :
            if not current :
                return 0
            return max(dfs(current.left), dfs(current.right))+1
        
        return dfs(root)