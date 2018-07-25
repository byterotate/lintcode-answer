/**
 * @param A: an integer sorted array
 * @param target: an integer to be inserted
 * @return: a list of length 2, [index1, index2]
 */
const searchRange = function (A, target) {
  const searchFirst = function (A, target, start, end) {
    if (start + 1 >= end) {
      if (A[start] === target) {
        return start
      }
      if (A[end] === target) {
        return end
      }
      return -1
    }
    const mid = Math.floor(start / 2 + end / 2)
    if (A[mid] >= target) {
      return searchFirst(A, target, start, mid)
    }
    return searchFirst(A, target, mid, end)
  }
  const searchLast = function (A, target, start, end) {
    if (start + 1 >= end) {
      if (A[end] === target) {
        return end
      }
      if (A[start] === target) {
        return start
      }
      return -1
    }
    const mid = Math.floor((start + end) / 2)
    if (A[mid] <= target) {
      return searchLast(A, target, mid, end)
    }
    return searchLast(A, target, start, mid)
  }

  return [searchFirst(A, target, 0, A.length - 1), searchLast(A, target, 0, A.length - 1)]

}
