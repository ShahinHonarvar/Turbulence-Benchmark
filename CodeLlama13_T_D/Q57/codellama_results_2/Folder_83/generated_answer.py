
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            curr_row = i
            curr_col = j
            while curr_row < rows and curr_col < cols:
                if matrix[curr_row][curr_col] == -15:
                    return [matrix[i:curr_row, j:curr_col]]
                else:
                    break
    return []
