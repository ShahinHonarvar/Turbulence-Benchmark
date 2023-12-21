
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for sub_x in range(1, rows + 1):
        for sub_y in range(1, cols + 1):
            for i in range(rows - sub_x + 1):
                for j in range(cols - sub_y + 1):
                    submatrix = matrix[i:i + sub_x, j:j + sub_y]
                    if np.size(submatrix) == 122:
                        count += 1
    return count
