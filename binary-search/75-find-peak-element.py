class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    [1, 2, 1, 3, 4, 5, 7, 6]返回1, 即数值 2 所在位置, 或者6, 即数值 7 所在位置.
    """
    def findPeak(self, A):
      return self._innerFindPeak(A, 0, len(A))
    def _innerFindPeak(self, A, start, end):
      mid = (start + end) // 2
      deltaMidLeft = A[mid] - A[mid - 1]
      deltaMidRight = A[mid] - A[mid + 1]
      if deltaMidLeft > 0 and deltaMidRight > 0:
        return mid
      if deltaMidLeft <= 0:
        return self._innerFindPeak(A, start, mid)
      if deltaMidRight <= 0:
        return self._innerFindPeak(A, mid, end)