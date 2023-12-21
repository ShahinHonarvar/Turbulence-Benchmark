
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 29 integers
    count = 0
    
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[i])):
            # Initialize a temporary list to store the elements of the submatrix
            temp = []
            
            # Iterate over the rows and columns of the submatrix
            for k in range(i, i + 29):
                for l in range(j, j + 29):
                    # If the element is not out of bounds, add it to the temporary list
                    if k < len(matrix) and l < len(matrix[k]):
                        temp.append(matrix[k][l])
            
            # If the number of elements in the submatrix is equal to 29, increment the counter
            if len(temp) == 29:
                count += 1
    
    return count
