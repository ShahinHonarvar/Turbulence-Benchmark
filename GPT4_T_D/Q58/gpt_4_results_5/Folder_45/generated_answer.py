
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = np.shape(matrix)

    for i in range(nrows):
        for j in range(ncols):
            for m in range(i+1, nrows+1):
                for n in range(j+1, ncols+1):
                    submatrix = matrix[i:m, j:n]
                    if np.size(submatrix) == 28:
                        count +=1
    
    return count
