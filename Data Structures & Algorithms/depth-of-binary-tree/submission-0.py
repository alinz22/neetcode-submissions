# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
         # --- 1. Recursive DFS (Elegant and common) ---
            if not root:
                return 0

            leftD = self.maxDepth(root.left)
            rightD = self.maxDepth(root.right)

            return 1 + max(leftD, rightD)


        # --- 2. BFS (Level Order Traversal) ---
        # from collections import deque
        # if not root:
        #     return 0
        # queue = deque([root])
        # depth = 0
        # while queue:
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     depth += 1
        # return depth

        # --- 3. Iterative DFS with Stack ---
        # if not root:
        #     return 0
        # stack = [(root, 1)]
        # max_depth = 0
        # while stack:
        #     node, depth = stack.pop()
        #     if node:
        #         max_depth = max(max_depth, depth)
        #         stack.append((node.left, depth + 1))
        #         stack.append((node.right, depth + 1))
        # return max_depth