"""
class SVNRepo:
    @classmethod
    def isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
bad version.
"""


class Solution:
    """
    @param: n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
      return self._innerFindFirstBadVersion(1, n)

    def _innerFindFirstBadVersion(self, start, end):
      if start + 1 >= end:
        if SVNRepo.isBadVersion(start):
          return start
        elif SVNRepo.isBadVersion(end):
          return end
        return -1
      mid = start + end // 2 - start // 2 # 防止溢出
      if SVNRepo.isBadVersion(mid):
        return self._innerFindFirstBadVersion(start, mid)
      return self._innerFindFirstBadVersion(mid, end)