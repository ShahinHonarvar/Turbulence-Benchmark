
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for sub_size in range(1, min(rows, cols) + 1):
        for i in range(rows - sub_size + 1):
            for j in range(cols - sub_size + 1):
                sub_matrix = matrix[i:i + sub_size, j:j + sub_size]
                if np.sum(sub_matrix) == 416:
                    result.append(sub_matrix)
    return result
