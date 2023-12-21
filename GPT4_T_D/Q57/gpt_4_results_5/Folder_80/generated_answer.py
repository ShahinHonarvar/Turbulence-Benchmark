
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, columns = matrix.shape
    submatrices = []

    for size in range(1, min(rows, columns) + 1):
        for x in range(rows - size + 1):
            for y in range(columns - size + 1):
                submatrix = matrix[x:x+size, y:y+size]

                if submatrix.sum() == 245:
                    submatrices.append(submatrix)

    return submatrices
