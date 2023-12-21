
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices_equal_to_59 = []
    
    for sub_row in range(1,rows + 1):
        for sub_col in range(1,cols + 1):
            for i in range(0,rows - sub_row + 1):
                for j in range(0,cols - sub_col + 1):
                    submatrix = matrix[i:i + sub_row, j:j + sub_col]
                    if np.sum(submatrix) == 59:
                        submatrices_equal_to_59.append(submatrix)
    
    return submatrices_equal_to_59
