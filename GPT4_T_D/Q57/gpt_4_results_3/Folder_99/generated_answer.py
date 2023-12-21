
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    no_of_rows, no_of_columns = matrix.shape
    for x1 in range(no_of_rows):
        for y1 in range(no_of_columns):
            for x2 in range(x1, no_of_rows):
                for y2 in range(y1, no_of_columns):
                    submatrix = matrix[x1:x2+1, y1:y2+1]
                    if np.sum(submatrix) == -185:
                        result.append(submatrix)
    return result
