
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Calculate the sum of all integers in each row and column of the matrix
    row_sums = np.sum(matrix, axis=1)
    col_sums = np.sum(matrix, axis=0)
    
    # Find the submatrices with the desired sum
    submatrices = []
    for i in range(len(row_sums)):
        for j in range(len(col_sums)):
            if row_sums[i] + col_sums[j] == -255:
                # Create a new matrix with the same shape as the original matrix
                submatrix = np.zeros((len(row_sums), len(col_sums)))
                
                # Populate the submatrix with the desired sum
                for k in range(len(row_sums)):
                    for l in range(len(col_sums)):
                        if i <= k and j <= l:
                            submatrix[k][l] = matrix[k][l]
                            
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)
    
    return submatrices
