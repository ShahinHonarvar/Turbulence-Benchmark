
def submatrices_with_particular_sum(matrix):
    """
    Finds all submatrices of the given matrix such that the sum of all integers in each submatrix equals -261.
    If no such submatrix is found, returns an empty list.
    
    Args:
        matrix (numpy array): The two-dimensional numpy matrix of integers.
        
    Returns:
        list: A list of lists representing all submatrices with the desired sum. Each inner list contains the row and column indices of a submatrix.
    """
    # Initialize an empty list to store the results
    result = []
    
    # Loop through each submatrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    # Calculate the sum of all integers in the current submatrix
                    subsum = matrix[i:k+1, j:l+1].sum()
                    
                    # If the sum is equal to -261, add the submatrix to the results
                    if subsum == -261:
                        result.append([i, j, k, l])
    
    return result
