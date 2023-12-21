
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    if(np.size(matrix[i:k+1, j:l+1])==115):
                        count +=1
    return count
