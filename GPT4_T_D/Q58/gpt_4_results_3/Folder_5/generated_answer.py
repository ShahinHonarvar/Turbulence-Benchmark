
import numpy as np

def submatrix_with_n_numbers(matrix):
  count = 0
  rows, cols = matrix.shape
  for submatrix_height in range(1, rows+1):
    for submatrix_width in range(1, cols+1):
      if submatrix_height * submatrix_width == 63:
        for row in range(rows - submatrix_height + 1):
          for col in range(cols - submatrix_width + 1):
            count += 1
  return count
