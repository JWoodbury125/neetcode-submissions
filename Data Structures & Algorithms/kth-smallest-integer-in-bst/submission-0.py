# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        import heapq

        vals = []
        def traverse(node):
            if not node: return
            vals.append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        result = 0
        heapq.heapify(vals)
        for _ in range(k):
            result = heapq.heappop(vals)

        return result