class Solution:
    """
    这个解法不是时间复杂度合规的，O(2^n)会导致Time Limit Exceeded
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    
    """
    def minimumTotal(self, triangle):
      return self._minimumTotal(triangle, 0, 0)
    def _minimumTotal(self, triangle, Y, X):
      if Y == len(triangle) - 1:
        return triangle[Y][X]
      return min(self._minimumTotal(triangle, Y + 1, X), self._minimumTotal(triangle, Y + 1, X + 1)) + triangle[Y][X]

