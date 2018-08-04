/**
 * @param A: an integer array
 * @return: 
 */
const sortIntegers2 = function (A) {
  arr = A.splice(0)
  result = sort(arr)
  result.forEach(item => A.push(item))
}


function sort(A) {
  if (A.length <= 1) {
    return A
  }
  let left = []
  let right = []

  const mid = A.pop()

  A.forEach(item => {
      if(item < mid) {
        left.push(item)
      } else {
        right.push(item)
      }
  })
  const leftSorted = sort(left)
  const rightSorted = sort(right)
  return leftSorted.concat([mid]).concat(rightSorted)
}

const A = [3,2,1,4,5]
sortIntegers2(A)
