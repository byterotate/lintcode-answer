/**
 * @param matrix: matrix, a list of lists of integers
 * @param target: An integer
 * @return: a boolean, indicate whether matrix contains target
 * [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
  ]
 */
const searchMatrix = function (matrix, target, start = 0, end = null) {
  if (end === null) {
    end = matrix.length - 1
  }
  if (matrix.length === 0) {
    return false
  }
  if (matrix[0].length === 0) {
    return false
  }
  if (start + 1 >= end) {
    if (matrix[start] && matrix[start][0] <= target && matrix[start][matrix[start].length - 1] >= target) {
      return searchArray(matrix[start], target)
    }
    if (matrix[end] && matrix[end][0] <= target && matrix[end][matrix[end].length - 1] >= target) {
      return searchArray(matrix[end], target)
    }
    return false
  }
  const mid = Math.floor(start / 2 + end / 2)
  const midArray = matrix[mid]

  if (midArray[0] <= target && mid[midArray.length - 1] >= target) {
    return searchArray(midArray, target)
  } else if (midArray[0] > target) {
    return searchMatrix(matrix, target, start, mid - 1)
  } else {
    return searchMatrix(matrix, target, mid + 1, end)
  }
}

const searchArray = function (arr, target, start = 0, end = null) {
  if (end === null) {
    end = arr.length - 1
  }
  if (start + 1 >= end) {
    if (arr[start] === target) return true
    if (arr[end] === target) return true
    return false
  }
  const mid = Math.floor(start / 2 + end / 2)

  if (arr[mid] === target) {
    return true
  } else if (arr[mid] < target) {
    return searchArray(arr, target, mid + 1, end)
  } else {
    return searchArray(arr, target, start, mid - 1)
  }
}

