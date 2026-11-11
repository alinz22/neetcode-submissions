# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxOfPath):
            if not root:
                return 0
            
            if root.val >= maxOfPath:
                res = 1
            else:
                res = 0
            
            maxOfPath = max(maxOfPath, root.val)

            res += dfs(root.left, maxOfPath)
            res += dfs(root.right, maxOfPath)
            return res

        return dfs(root, root.val)


        


