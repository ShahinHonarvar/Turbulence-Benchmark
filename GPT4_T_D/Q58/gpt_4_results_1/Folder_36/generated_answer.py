
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for sub_x in range(rows):
        for sub_y in range(cols):
            for x in range(rows - sub_x + 1):
                for y in range(cols - sub_y + 1):
                    if np.prod(matrix[x:x + sub_x, y:y + sub_y].shape) == 131:
                        count += 1
    return count
