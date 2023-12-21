
def submatrix_with_particular_sum(mat):
    # Initialize the result list
    res = []
    
    # Iterate over each submatrix of the given matrix
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            for k in range(i, len(mat)):
                for l in range(j, len(mat[0])):
                    
                    # Check if the sum of all integers in each submatrix is equal to 1
                    if mat[k][l] == 1:
                        
                        # Add the submatrix to the result list
                        res.append(mat[i:k+1, j:l+1])
    
    return res
