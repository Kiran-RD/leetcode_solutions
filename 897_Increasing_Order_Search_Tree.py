# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.head = self.tail = TreeNode()

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            self.tail.right = node
            self.tail = self.tail.right
            self.tail.left = None
            dfs(node.right)

        dfs(root)
        return self.head.right
