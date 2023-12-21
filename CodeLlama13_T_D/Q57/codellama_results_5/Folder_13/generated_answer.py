
def submatrix_with_particular_sum(matrix):
    # Initialize the list of all submatrices that meet the condition
    submatrices = []
    
    # Iterate over each row in the matrix
    for i in range(len(matrix)):
        # Iterate over each column in the matrix
        for j in range(len(matrix[0])):
            # Initialize the current submatrix with the first element
            current_submatrix = [[matrix[i][j]]]
            
            # Iterate over the remaining elements in the row and column
            for k in range(i+1, len(matrix)):
                for l in range(j+1, len(matrix[0])):
                    # Add the current element to the submatrix if it is not already there
                    if matrix[k][l] not in current_submatrix:
                        current_submatrix.append([matrix[k][l]])
            
            # Check if the sum of all integers in the submatrix equals 382
            if sum(map(sum, current_submatrix)) == 382:
                # Add the submatrix to the list of all submatrices that meet the condition
                submatrices.append(current_submatrix)
    
    # Return the list of all submatrices that meet the condition
    return submatrices
