
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i, j] == 20:
                if i + 1 >= rows or j + 1 >= cols:
                    continue
                submatrix = matrix[i:i+2, j:j+2]
                if np.size(submatrix) == 4:
                    count += 1
    return count
