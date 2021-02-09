# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Using reverse inorder traversal

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.curr_sum = 0

        def dfs(node):
            if not node:
                return

            dfs(node.right)
            self.curr_sum += node.val
            node.val = self.curr_sum
            dfs(node.left)

            return node

        return dfs(root)

#----------------------------------------------------------------------------------------
# kind of Brute Force

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        elements = self.dfs(root)
        self.elements_sorted = sorted(elements)
        return self.replace(root)

    def dfs(self, node):
        if not node:
            return []

        lst = []

        lst += self.dfs(node.left)
        lst.append(node.val)
        lst += self.dfs(node.right)
        return lst

    def replace(self, node):
        if not node:
            return

        self.replace(node.left)
        node.val = self.get_sum(node.val)
        self.replace(node.right)
        return node

    def get_sum(self, val):
        n = r = len(self.elements_sorted) - 1
        l = 0
        i = 0
        while l <= r:
            mid = (l + r) // 2
            if self.elements_sorted[mid] == val:
                while mid > 0 and self.elements_sorted[mid - 1] == val:
                    mid -= 1
                i = mid
                break
            elif val > self.elements_sorted[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return sum(self.elements_sorted[i:])