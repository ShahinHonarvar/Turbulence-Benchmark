
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    subarrays_sizes = [(a, b) 
                    for a in range(matrix.shape[0]+1) 
                    for b in range(matrix.shape[1]+1) 
                    if a * b == 175]
    
    for size in subarrays_sizes:
        a, b = size
        for x in range(matrix.shape[0] - a + 1):
            for y in range(matrix.shape[1] - b + 1):
                submatrix = matrix[x:x+a,y:y+b]
                if submatrix.size == 175:
                    count += 1
    return count
