
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[0])):
            # Initialize a temporary list to store the submatrix elements
            temp = []
            
            # Iterate over each row of the submatrix
            for k in range(i, len(matrix)):
                # Iterate over each column of the submatrix
                for l in range(j, len(matrix[0])):
                    # Add the element to the temporary list
                    temp.append(matrix[k][l])
            
            # Check if the sum of all elements in the temporary list is 15
            if sum(temp) == 15:
                # Add the submatrix to the results list
                results.append(temp)
    
    # Return the results list
    return results
