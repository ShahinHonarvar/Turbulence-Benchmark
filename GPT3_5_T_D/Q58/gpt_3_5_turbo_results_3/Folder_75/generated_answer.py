
import numpy as np

def submatrix_with_n_numbers(mat):
    rows, cols = mat.shape
    count = 0
    for i in range(rows - 7):
        for j in range(cols - 9):
            submat = mat[i:i+8, j:j+10]
            if len(submat.flatten()) == 80:
                count += 1
    return count
