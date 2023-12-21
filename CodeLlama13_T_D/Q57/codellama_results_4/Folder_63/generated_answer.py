
def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices with sum equal to 64
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[0])):
            # Initialize a temporary list to store the elements of the submatrix
            temp = []
            
            # Add the element at the current position (i, j) to the temporary list
            temp.append(matrix[i][j])
            
            # Loop through each row and column that is below and to the right of the current position
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix[0])):
                    # Add the element at the current position (k, l) to the temporary list
                    temp.append(matrix[k][l])
            
            # Check if the sum of all elements in the submatrix is equal to 64
            if sum(temp) == 64:
                # If so, add the submatrix to the list of submatrices with sum equal to 64
                submatrices.append(temp)
    
    return submatrices
