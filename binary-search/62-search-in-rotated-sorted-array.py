class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
      # write your code here
      if len(A) == 0:
        return -1
      return self.__search(A, target, 0, len(A) - 1)

    def __searchNormal(self, A, target, start, end):
      if start + 1 >= end:
        return start if target == A[start] else end if target == A[end] else -1
      mid = (start + end) // 2
      if A[mid] == target:
        return mid
      if A[mid] > target:
        return self.__searchNormal(A, target, start, mid)
      return self.__searchNormal(A, target, mid, end)

    def __search(self, A, target, start, end):
      if start + 1 >= end:
        return start if target == A[start] else end if target == A[end] else -1
      if A[start] <= A[end]:
        return self.__searchNormal(A, target, start, end) 
      
      mid = (start + end) // 2
      print(start, mid, end)
      if mid == target:
        return mid
      if A[mid] < A[end]: # 后半部分是顺序的
        if target >= A[mid] and target <= A[end]:
          return self.__searchNormal(A, target, mid, end)
        return self.__search(A, target, start, mid)
      if A[mid] > A[start]: # 前半部分是顺序的
        if target <= A[mid] and target >= A[start]:
          return self.__searchNormal(A, target, start, mid)
        return self.__search(A, target, mid, end)

if __name__ == '__main__':
    s = Solution()
    print(s.search([1001,10001,10007,1,10,101,201], 10001))