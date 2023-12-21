
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    for submatrix_height in range(1,rows + 1):
        for submatrix_width in range(1, cols + 1):
            for row in range(rows - submatrix_height + 1):
                for col in range(cols - submatrix_width + 1):
                    submatrix = matrix[row:row+submatrix_height, col:col+submatrix_width]
                    if np.sum(submatrix) == 27:
                        submatrices.append(submatrix)
    
    return submatrices
