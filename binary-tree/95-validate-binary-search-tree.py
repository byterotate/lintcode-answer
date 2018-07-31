"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
      if root is None:
        return True
      # if root.left is None and root.right is None:
      #   return True
      leftIsValid = self.isValidBST(root.left)
      rightIsValid = self.isValidBST(root.right)
      if leftIsValid and rightIsValid:
        flag = True
        if root.left:
          flag = flag and root.val > self._maxInBst(root.left)
        if root.right: 
          flag = flag and root.val < self._minInBst(root.right)
        return flag
      return False
    def _minInBst(self, root):
      while root.left:
        root = root.left
      return root.val
    
    def _maxInBst(self, root):
      while root.right:
        root = root.right
      return root.val