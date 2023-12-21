
def submatrix_with_particular_sum(mat):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each row of the matrix
    for i in range(len(mat)):
        # Iterate over each column of the matrix
        for j in range(len(mat[0])):
            # Calculate the sum of all integers in the submatrix starting from (i, j)
            curr_sum = 0
            for k in range(i, len(mat)):
                for l in range(j, len(mat[0])):
                    curr_sum += mat[k][l]
            
            # If the sum is equal to -57, add the submatrix to the result list
            if curr_sum == -57:
                result.append((i, j))
    
    return result
