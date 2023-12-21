import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+119] == list(range(i,j+1)), axis=1) for i in range(0,len(matrix)-118) for j in range(i+1,len(matrix)))
