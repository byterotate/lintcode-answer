class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
      self.cache = [[None for y in range(len(triangle[-1]))] for x in range(len(triangle))]
      return self._minimumTotal(triangle, 0, 0)
    def _minimumTotal(self, triangle, Y, X):
      if Y == len(triangle) - 1:
        return triangle[Y][X]
      if self.cache[Y+1][X]:
        below = self.cache[Y+1][X]
      else:
        below = self.cache[Y+1][X] = self._minimumTotal(triangle, Y+1, X)

      if self.cache[Y+1][X+1]:
        belowRight = self.cache[Y+1][X+1]
      else:
        belowRight = self.cache[Y+1][X+1] = self._minimumTotal(triangle, Y+1, X+1)
      return min(belowRight, below) + triangle[Y][X]