
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Convert the matrix to a 1D numpy array
    flattened = np.ravel(matrix)
    
    # Find all contiguous sequences of length equal to the number of rows in the matrix
    rows = [flattened[i:i+np.size(matrix, axis=0)] for i in range(len(flattened)-np.size(matrix, axis=0)+1)]
    
    # Find all contiguous sequences of length equal to the number of columns in the matrix
    cols = [flattened[i:i+np.size(matrix, axis=1)] for i in range(len(flattened)-np.size(matrix, axis=1)+1)]
    
    # Find all submatrices by iterating over the rows and columns
    submatrices = []
    for row in rows:
        for col in cols:
            if np.sum(row) == 432 and np.sum(col) == 432:
                submatrices.append((row, col))
    
    # Return the list of all submatrices that have a particular sum of 432
    return submatrices
