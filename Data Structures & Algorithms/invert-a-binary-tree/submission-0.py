# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Define the base class to terminate recursion
        if not root: return

        # Swap the current left and right
        root.left, root.right = root.right, root.left

        # Begin recursion on the left side
        self.invertTree(root.left)

        # And the right
        self.invertTree(root.right)

        return root