
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []
    # Loop through each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a temporary submatrix with only one element
            temp_submatrix = np.array([[matrix[i,j]]]])

            # Loop through each row and column of the matrix starting from the current element
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the temporary submatrix
                    temp_submatrix = np.append(temp_submatrix, [[matrix[k,l]]]], axis=0)

                    # Check if the sum of all elements in the temporary submatrix is equal to 69
                    if np.sum(temp_submatrix) == 69:
                        # Add the temporary submatrix to the list of submatrices
                        submatrices.append(temp_submatrix)

                        # Break out of the inner loop since we have found a matching submatrix
                        break

                    # If the sum of all elements in the temporary submatrix is not equal to 69, continue searching
                    else:
                        continue

                    # Break out of the outer loop since we have found a matching submatrix
                    break

                # If the sum of all elements in the temporary submatrix is not equal to 69, continue searching
                else:
                    continue

            # If no matching submatrix was found, continue searching
            if len(submatrices) == 0:
                continue

            # If a matching submatrix was found, break out of the outer loop since we have found a matching submatrix
            else:
                break

        # If no matching submatrix was found, continue searching
        if len(submatrices) == 0:
            continue

        # If a matching submatrix was found, return the list of submatrices
        else:
            return submatrices

    # If no matching submatrix was found, return an empty list
    else:
        return []
