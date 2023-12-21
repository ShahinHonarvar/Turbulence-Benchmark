
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 83
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == n:
                for x in range(i, len(matrix)):
                    for y in range(j, len(matrix[0])):
                        submatrix = matrix[i:x+1, j:y+1]
                        if submatrix.size == n:
                            count += 1
    return count
