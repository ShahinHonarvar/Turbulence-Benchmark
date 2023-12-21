
import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_matrices = []
    rows, cols = matrix.shape
    for size_x in range(1, cols+1):
        for size_y in range(1, rows+1):
            for x in range(cols-size_x+1):
                for y in range(rows-size_y+1): 
                    sub_matrix = matrix[y:y+size_y, x:x+size_x]
                    if np.sum(sub_matrix) == -63:
                        sub_matrices.append(sub_matrix)
    if not sub_matrices:
        return []
    return sub_matrices
