# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0

        def dfs(node, level):
            nonlocal maxDepth
            if not node:
                return
            level += 1
            maxDepth = max(maxDepth, level)
            if node.left:
                dfs(node.left, level)
            if node.right:
                dfs(node.right, level)

        dfs(root, 0)
        return maxDepth
