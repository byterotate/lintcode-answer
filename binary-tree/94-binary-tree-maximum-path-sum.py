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
    @return: An integer
    """
    def maxPathSum(self, root):
      maxRootToAny, maxAnyToAny = self._maxPathSum(root)
      return maxAnyToAny
    def _maxPathSum(self, root):
      if root is None:
        return (float("-inf"), float("-inf"))
      leftRootToAny, leftAnyToAny = self._maxPathSum(root.left)
      rightRootToAny, rightAnyToAny = self._maxPathSum(root.right)
      maxRootToAny = max(leftRootToAny + root.val, rightRootToAny + root.val, root.val)
      maxAnyToAny = max(leftAnyToAny, rightAnyToAny, leftRootToAny + rightRootToAny + root.val, maxRootToAny)
      return (maxRootToAny, maxAnyToAny)

