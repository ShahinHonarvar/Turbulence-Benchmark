 
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i,j] == 63:
                submatrix = matrix[i:, j:]
                sub_rows, sub_cols = submatrix.shape
                if sub_rows >= 7 and sub_cols >= 9:
                    for x in range(sub_rows - 6):
                        for y in range(sub_cols - 8):
                            if np.count_nonzero(submatrix[x:x + 7, y:y + 9] == 63) == 63:
                                count += 1
    return count
