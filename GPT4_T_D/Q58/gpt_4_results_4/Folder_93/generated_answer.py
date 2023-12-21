
import numpy as np

def submatrix_with_n_numbers(np_matrix):
    count = 0
    for i in range(np_matrix.shape[0]):
        for j in range(np_matrix.shape[1]):
            for m in range(i, np_matrix.shape[0]):
                for n in range(j, np_matrix.shape[1]):
                    if ((m-i+1)*(n-j+1)) == 53:
                        count += 1
    return count
