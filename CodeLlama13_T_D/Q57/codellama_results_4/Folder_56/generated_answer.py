
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Convert the matrix to a list of lists for easier iteration
    matrix = matrix.tolist()
    
    # Initialize an empty list to store the found submatrices
    submatrices = []
    
    # Iterate over each row in the matrix
    for i in range(len(matrix)):
        # Iterate over each column in the current row
        for j in range(len(matrix[i])):
            # Initialize a temporary list to store the submatrix elements
            temp = []
            
            # Iterate over each row in the matrix from the current row to the bottom
            for k in range(i, len(matrix)):
                # Iterate over each column in the current row to the right of the current column
                for l in range(j, len(matrix[k])):
                    # Add the element at (k, l) to the temporary list
                    temp.append(matrix[k][l])
                    
                    # If the sum of all elements in the temporary list is -50, add it to the submatrices list
                    if sum(temp) == -50:
                        submatrices.append(temp.copy())
                        
    return submatrices
