
import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    rows, columns = matrix.shape

    # Check all possible submatrices
    for i in range(rows):
        for j in range(columns):
            for k in range(i+1, rows+1):
                for l in range(j+1, columns+1):
                    # Compare sum of current submatrix to desired sum
                    if np.sum(matrix[i:k,j:l]) == -82:
                        results.append(matrix[i:k,j:l])
    
    return results
