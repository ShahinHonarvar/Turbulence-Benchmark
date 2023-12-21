import numpy as np
def submatrix_with_particular_sum(matrix):
    return [submatrix for i in range(len(matrix)-1) for j in range(len(matrix[0])-1) for submatrix in np.split(matrix[:i]+matrix[i+1:], matrix[i], axis=0)+np.split(matrix[:,:j]+matrix[:,j+1:], matrix[:,j], axis=1)] if -3 in submatrix]
