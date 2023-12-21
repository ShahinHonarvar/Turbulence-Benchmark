
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 175
    count = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == n:
                for x in range(i, len(matrix)):
                    for y in range(j, len(matrix[0])):
                        if np.sum(matrix[i:x+1, j:y+1]) == n * ((x-i+1)*(y-j+1)):
                            count += 1
    
    return count
