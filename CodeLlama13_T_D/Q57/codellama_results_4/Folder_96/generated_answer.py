
def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices with sum -63
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix
            temp_submatrix = []
            
            # Loop through each row and column of the submatrix
            for k in range(i, matrix.shape[0]):
                temp_row = []
                for l in range(j, matrix.shape[1]):
                    # Add the element to the temporary list if it is not equal to -63
                    if matrix[k][l] != -63:
                        temp_row.append(matrix[k][l])
                    
                # If the sum of the elements in the submatrix is equal to -63, add it to the list of submatrices
                if sum(temp_row) == -63:
                    submatrices.append(temp_submatrix)
            
    # Return the list of all submatrices with sum -63
    return submatrices
