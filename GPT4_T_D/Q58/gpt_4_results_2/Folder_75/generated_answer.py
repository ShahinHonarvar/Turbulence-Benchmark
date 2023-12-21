
import numpy as np

def submatrix_with_n_numbers(matrix):
    total_count = 0
    num_rows, num_cols = np.shape(matrix)
    
    for submatrix_rows in range(1, num_rows + 1):
        for submatrix_cols in range(1, num_cols + 1):
            if submatrix_rows * submatrix_cols == 80:
                for i in range(num_rows - submatrix_rows + 1):
                    for j in range(num_cols - submatrix_cols + 1):
                        total_count += 1
    return total_count
