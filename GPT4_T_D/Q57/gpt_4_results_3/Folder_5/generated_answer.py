
import numpy as np

def submatrix_with_particular_sum(np_matrix):
    rows, columns = np_matrix.shape
    submatrices=[]

    for submatrix_height in range(1, rows + 1):
        for submatrix_width in range(1, columns + 1):
            for i in range(rows - submatrix_height + 1):
                for j in range(columns - submatrix_width + 1):
                    submatrix = np_matrix[i:i + submatrix_height, j:j + submatrix_width]
                    if np.sum(submatrix) == -43:
                        submatrices.append(submatrix)
                        
    return submatrices
