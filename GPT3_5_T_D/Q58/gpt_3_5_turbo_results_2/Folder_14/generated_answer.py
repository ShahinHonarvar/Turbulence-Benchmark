
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + 3 <= rows and j + 3 <= cols:
                submatrix = matrix[i:i+3, j:j+3].flatten().tolist()
                if submatrix.count(84) == 9:
                    count += 1
    return count
