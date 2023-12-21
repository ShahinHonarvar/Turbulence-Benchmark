
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, columns = matrix.shape
    submatrices = []
    for size_i in range(1,rows+1):
        for size_j in range(1,columns+1):    
            for i in range(rows-size_i+1):
                for j in range(columns-size_j+1):
                    submatrix = matrix[i:(i+size_i), j:(j+size_j)]
                    if np.sum(submatrix) == 54:
                        submatrices.append(submatrix)
    return submatrices
