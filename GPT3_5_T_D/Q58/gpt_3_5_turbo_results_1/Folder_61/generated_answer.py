
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            if (matrix[i,j]+matrix[i+1,j]+matrix[i,j+1]+matrix[i+1,j+1]) == 4:
                count += 1
    
    return count
