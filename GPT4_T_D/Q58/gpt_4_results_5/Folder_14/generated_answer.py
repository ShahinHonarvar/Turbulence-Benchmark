
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    
    for r in range(matrix.shape[0]):
        for c in range(matrix.shape[1]):
            for w in range(c+1, matrix.shape[1]+1):
                for h in range(r+1, matrix.shape[0]+1):
                    submatrix = matrix[r:h, c:w]
                    if np.size(submatrix)==84:
                        count+=1
    return count
