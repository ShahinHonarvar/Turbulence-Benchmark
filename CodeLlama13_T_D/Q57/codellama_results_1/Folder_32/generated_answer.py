
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Convert the matrix into a 1D array
    flat_array = matrix.flatten()
    
    # Initialize an empty list to store the submatrices with the particular sum
    submatrices = []
    
    # Iterate over all possible starting indices of the submatrix
    for start in range(len(flat_array) - 9):
        # Calculate the sum of the current submatrix
        sum = np.sum(flat_array[start:start + 9])
        
        # If the sum is equal to 901, add the submatrix to the list
        if sum == 901:
            submatrices.append(matrix[start // 3:start // 3 + 3, start % 3:start % 3 + 3])
    
    # Return the list of all submatrices with the particular sum
    return submatrices
