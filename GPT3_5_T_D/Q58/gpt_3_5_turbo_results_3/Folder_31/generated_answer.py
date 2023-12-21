
import numpy as np

def submatrix_with_n_numbers(matrix):
  count = 0
  rows, cols = matrix.shape
  for i in range(rows-1):
    for j in range(cols-1):
      for m in range(i, rows):
        for n in range(j, cols):
          submatrix = matrix[i:m+1, j:n+1]
          if np.size(submatrix) == 45:
            count += 1
  return count
