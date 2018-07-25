/**
 * @param nums: The integer array.
 * @param target: Target to find.
 * @return: The first position of target. Position starts from 0.
 */
const binarySearch = function (nums, target, start = 0, end = null) {
  if (end === null) {
    end = nums.length -1
  }
  if (start + 1 >= end) {
    if (nums[start] === target) return start
    if (nums[end] === target) return end
    return -1
  }
  const mid = Math.floor(start / 2 + end / 2)
  if (nums[mid] >= target) {
    return binarySearch(nums, target, start, mid)
  }
  return binarySearch(nums, target, mid, end)
}
