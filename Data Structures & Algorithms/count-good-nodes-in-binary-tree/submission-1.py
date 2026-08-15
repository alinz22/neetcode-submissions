# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxValue):
            if not root:
                return 0

            if root.val >= maxValue:
                res = 1 
            else:
                res = 0
            maxValue =  max(root.val, maxValue)
            childrenVals = dfs(root.left, maxValue) + dfs(root.right, maxValue)
    
            return res + childrenVals
        
        return dfs(root, root.val)
