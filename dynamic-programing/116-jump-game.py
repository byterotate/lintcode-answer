class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
      answerSpace = [False for _ in range(len(A))]
      answerSpace[0] = True
      i = 0
      while i < len(A):
        if answerSpace[i] is True:
          canGoStep = A[i]
          j = 1
          while j <= canGoStep:
            if j + i >= len(A):
              break
            answerSpace[j + i] = True
            j = j + 1
        i = i + 1
      print(answerSpace)
      return answerSpace[-1]

if __name__ == '__main__':
  s = Solution()
  print(s.canJump([0,8,2,0,9]))