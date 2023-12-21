
import numpy as np

def submatrix_with_particular_sum(matrix):
    num_rows, num_cols = np.shape(matrix)
    submatrices_list = []
    
    # Iterate over the possible sizes of submatrices
    for submatrix_size in range(1, min(num_rows, num_cols)+1):
        # Iterate over the possible starting points of the submatrices
        for i in range(0, num_rows - submatrix_size + 1):
            for j in range(0, num_cols - submatrix_size + 1):
                # Extract the submatrix
                submatrix = matrix[i:i+submatrix_size, j:j+submatrix_size]
                # Check if its sum is 35
                if np.sum(submatrix) == 35:
                    submatrices_list.append(submatrix)
                    
    return submatrices_list
