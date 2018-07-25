/**
 * @param A: an integer sorted array
 * @param target: an integer to be inserted
 * @return: An integer
 */
const searchInsert = function (A, target, start = 0, end = null) { // firstBigger than target
  if (end === null) {
    end = A.length - 1
  }
  if (A.length === 0) {
    return 0
  }
  if (start + 1 >= end) {
    if (A[start] >= target) {
      return start
    }
    if (A[start] < target && A[end] >= target) {
      return end
    }
    if (A[end] < target) {
      return end + 1
    }
  }
  
  const mid = Math.floor(start/2 + end/2)
  if (A[mid] > target) {
    return searchInsert(A, target, start, mid)
  }
  return searchInsert(A, target, mid, end)
}

searchInsert([], 9)