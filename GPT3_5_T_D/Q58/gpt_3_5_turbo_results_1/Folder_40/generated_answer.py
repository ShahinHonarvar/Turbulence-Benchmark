
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 1:
                count += 1
                for x in range(i+1, rows):
                    for y in range(j+1, cols):
                        if matrix[x, y] == 1:
                            count += 1
                        else:
                            break
                    else:
                        continue
                    break
    return count
