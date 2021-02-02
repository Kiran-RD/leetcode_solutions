# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        if root.val < low:
            return root.right

        if high < root.val:
            return root.left

        return root