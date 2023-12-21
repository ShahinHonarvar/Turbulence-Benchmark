
import numpy as np

def submatrix_with_n_numbers(arr):
    count = 0
    if arr.size < 146:
        return 0
    for rows in range(arr.shape[0]):
        for cols in range(arr.shape[1]):
            for sub_rows in range(rows+1, arr.shape[0]+1):
                for sub_cols in range(cols+1, arr.shape[1]+1):
                    submatrix = arr[rows:sub_rows, cols:sub_cols]
                    if submatrix.size == 146:
                        count += 1
    return count
