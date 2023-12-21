
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[0])):
            # Initialize a temporary list to store the current submatrix
            temp = []
            
            # Add the current element to the temporary list
            temp.append(matrix[i][j])
            
            # Iterate over each row below the current row
            for k in range(i+1, len(matrix)):
                # Add the current element to the temporary list
                temp.append(matrix[k][j])
                
                # If the sum of all elements in the temporary list is equal to -81, add it to the result list
                if sum(temp) == -81:
                    result.append(temp)
            
            # Iterate over each column to the right of the current column
            for l in range(j+1, len(matrix[0])):
                # Add the current element to the temporary list
                temp.append(matrix[i][l])
                
                # If the sum of all elements in the temporary list is equal to -81, add it to the result list
                if sum(temp) == -81:
                    result.append(temp)
    
    # Return the result list
    return result
