# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Find a path where the values equal the taret sum

        # Got to another branch if nothing is being returned
        if root is None: return False

        if root.left is None and root.right is None:
            # Return whether the node is the target value or not
            return root.val == targetSum
        
        remainingSum = targetSum - root.val

        # Iterate through left and right branches
        return(self.hasPathSum(root.left, remainingSum) 
            or self.hasPathSum(root.right, remainingSum))

