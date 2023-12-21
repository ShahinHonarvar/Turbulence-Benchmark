
import numpy as np
def submatrix_with_particular_sum(mat):
    # Convert the matrix to a list of lists
    lst = mat.tolist()
    # Initialize an empty list to store the results
    result = []
    # Loop through each submatrix in the original matrix
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            # Get the current submatrix
            curr_submat = lst[i][j:]
            # Check if the sum of all integers in the current submatrix is 56
            if np.sum(curr_submat) == 56:
                # If so, add it to the result list
                result.append(curr_submat)
    return result
