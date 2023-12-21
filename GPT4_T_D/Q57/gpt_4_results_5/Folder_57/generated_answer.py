
import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = 13
    sub_matrices = []
    rows, cols = matrix.shape
        
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(rows):
                for y2 in range(cols):
                    if x2 >= x1 and y2 >= y1:
                        sub_matrix = matrix[x1:x2+1, y1:y2+1]
                        if sub_matrix.sum() == target_sum:
                            sub_matrices.append(sub_matrix.tolist())
    return sub_matrices
