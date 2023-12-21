
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for row in range(rows):
        for col in range(columns):
          for h in range(1, rows - row + 1):
            for w in range(1, columns - col + 1):
              if len(matrix[row:row+h, col:col+w].flatten()) == 107:
                count += 1
    return count
