
def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 147 integers
    count = 0
    
    # Iterate over each row in the matrix
    for i in range(len(matrix)):
        # Iterate over each column in the matrix
        for j in range(len(matrix[i])):
            # Check if the current element is 147
            if matrix[i][j] == 147:
                # Initialize a temporary counter for the number of integers in the submatrix
                temp_count = 0
                
                # Iterate over each row below the current row
                for k in range(i+1, len(matrix)):
                    # Check if the current element is 147
                    if matrix[k][j] == 147:
                        temp_count += 1
                    
                    # If the temporary counter reaches 147, increment the main counter and break out of the loop
                    if temp_count == 147:
                        count += 1
                        break
                        
                # If the main counter is not zero, break out of the outer loop
                if count > 0:
                    break
    
    return count
