
import numpy as np

def submatrix_with_particular_sum(arr):
    rows, cols = arr.shape
    result = []

    for top_row in range(rows):
        for top_col in range(cols):
            for bottom_row in range(top_row, rows):
                for bottom_col in range(top_col, cols):
                    submatrix = arr[top_row:bottom_row+1, top_col:bottom_col+1]
                    if np.sum(submatrix) == 0:
                        result.append(submatrix.tolist())

    return result
