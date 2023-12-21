
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for sub_x in range(1, rows + 1):
        for sub_y in range(1, cols + 1):
            for x in range(rows - sub_x + 1):
                for y in range(cols - sub_y + 1):
                    sub_matrix = matrix[x:x+sub_x, y:y+sub_y]
                    if np.sum(sub_matrix) == 80:
                        result.append(sub_matrix.tolist())
    return result
