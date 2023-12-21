
import numpy as np

def submatrix_with_n_numbers(input_matrix):
    count = 0
    rows, cols = input_matrix.shape
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            for i in range(rows - r + 1):
                for j in range(cols - c + 1):
                    if np.size(input_matrix[i: i + r, j: j + c]) == 107:
                        count += 1
    return count
