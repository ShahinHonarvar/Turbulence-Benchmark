
import numpy as np

def submatrix_with_particular_sum(matrix):
    output = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for x in range(row, len(matrix)):
                for y in range(col, len(matrix[0])):
                    submatrix = matrix[row:x+1, col:y+1]
                    if np.sum(submatrix) == -13:
                        output.append(submatrix)
    return output
