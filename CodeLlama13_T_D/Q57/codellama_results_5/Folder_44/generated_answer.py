
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Flatten the matrix into a 1D array
    flat_array = matrix.flatten()
    
    # Find all possible combinations of indices that sum to 830
    indices = []
    for i in range(len(flat_array)):
        for j in range(i, len(flat_array)):
            if np.sum(flat_array[i:j+1]) == 830:
                indices.append((i, j))
    
    # Extract the submatrices with the specified sum
    submatrices = []
    for i, j in indices:
        submatrix = matrix[i//matrix.shape[0]:j//matrix.shape[0]+1, i%matrix.shape[0]:j%matrix.shape[0]+1]
        submatrices.append(submatrix)
    
    return submatrices
