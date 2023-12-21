
import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    rows, cols = mat.shape
    for x in range(rows):
        for y in range(cols):
            for dx in range(1, rows+1):
                for dy in range(1, cols+1):
                    if x+dx <= rows and y+dy <= cols:
                        if np.size(mat[x:x+dx, y:y+dy]) == 115:
                            count += 1
    return count
