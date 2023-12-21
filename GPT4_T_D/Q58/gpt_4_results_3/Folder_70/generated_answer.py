
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    num_rows, num_cols = matrix.shape
    for rows in range(1, num_rows + 1):
        for cols in range(1, num_cols + 1):
            for i in range(num_rows - rows + 1):
                for j in range(num_cols - cols + 1):
                    submatrix = matrix[i:i+rows, j:j+cols]
                    if np.product(submatrix.shape) == 173:
                        count += 1
    return count
