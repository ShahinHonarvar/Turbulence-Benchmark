
import numpy as np

def submatrix_with_particular_sum(matrix):
    output = []
    dimensions = matrix.shape
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            for k in range(i+1, dimensions[0]+1):
                for l in range(j+1, dimensions[1]+1):
                    submatrix = matrix[i:k, j:l].copy()
                    if np.sum(submatrix) == -64:
                        output.append(submatrix)
    return output
