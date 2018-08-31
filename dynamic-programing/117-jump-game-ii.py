class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
      answerSpace = [None for _ in range(len(A))]
      answerSpace[0] = 0

      i = 0
      while i < len(A):
        canGoStep = A[i]
        currentStep = answerSpace[i]
        if currentStep is None:
          i += 1
          continue
        j = 1
        while j <= canGoStep:
          if i + j >= len(A):
            break
          if answerSpace[i + j] is None:
            answerSpace[i + j] = currentStep + 1
          else:
            answerSpace[i + j] = min(answerSpace[i + j], currentStep + 1)
          j += 1
        i += 1
      return answerSpace[-1]
          
if __name__ == '__main__':
  s = Solution()
  print(s.jump([2,3,1,1,4]))