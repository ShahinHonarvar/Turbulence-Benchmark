
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)-185):
        for j in range(len(matrix[0])-185):
            if all(x==186 for x in matrix[i:i+186,j:j+186].flatten()):
                count += 1
    return count
