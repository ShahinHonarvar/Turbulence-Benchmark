
def submatrix_with_n_numbers(mat):
    # Initialize a count variable to keep track of the number of submatrices with 69 integers
    count = 0
    
    # Iterate over each row and column of the matrix
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            # Initialize a temporary matrix to store the current submatrix
            temp_mat = [[0] * len(mat[i]) for _ in range(len(mat))]
            
            # Fill the temporary matrix with the elements of the original matrix
            for k in range(i, len(mat)):
                for l in range(j, len(mat[k])):
                    temp_mat[k][l] = mat[k][l]
            
            # Check if the current submatrix has 69 integers
            if sum(temp_mat.flatten()) == 69 * len(mat):
                count += 1
    
    return count
