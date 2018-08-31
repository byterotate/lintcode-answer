class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
      return self.__findMin(nums, 0, len(nums) -1)
    def __findMin(self, nums, start, end):
      if start + 1 >= end:
        return min(nums[start], nums[end])
      mid = (end + start) // 2
      print(start, mid, end)
      if nums[mid] > nums[end]:
        return self.__findMin(nums, mid, end)
      else:
        return self.__findMin(nums, start, mid)


if __name__ == '__main__':
  s = Solution()
  print(s.findMin([4,5,6,7,0,1,2]))