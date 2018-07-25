/**
 * @param matrix: A list of lists of integers
 * @param target: An integer you want to search in matrix
 * @return: An integer indicate the total occurrence of target in the given matrix
 */
const searchMatrix = function (matrix, target, curCol = 0, curRow = null) {
  if (curRow === null) {
    curRow = matrix.length - 1
  }
  if (matrix.length === 0) {
    return 0
  }
  if (matrix[0].length === 0) {
    return 0
  }
  if (curCol > matrix[0].length - 1 || curRow < 0) {
    return 0
  }

  const curValue = matrix[curRow][curCol]

  if (curValue === target) {
    return searchMatrix(matrix, target, curCol + 1, curRow - 1) + 1
  } else if (curValue < target) {
    return searchMatrix(matrix, target, curCol + 1, curRow)
  } else {
    return searchMatrix(matrix, target, curCol, curRow - 1)
  }
}
