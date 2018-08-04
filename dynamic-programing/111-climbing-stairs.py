class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
      result = [1, 1]
      i = 2
      if n == 0:
        return 0
      if n < 2:
        return result[n]
      while i <= n:
        result.append(result[i - 1] + result[i - 2])
        i += 1
      return result[n]

if __name__ == '__main__':
  s = Solution()
  print(s.climbStairs(5))