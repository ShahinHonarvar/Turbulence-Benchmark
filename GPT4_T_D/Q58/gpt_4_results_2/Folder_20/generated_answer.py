
import numpy as np

def submatrix_with_n_numbers(arr):
    counter = 0
    rows, cols = arr.shape
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            submatrices = [
                arr[i:i+row, j:j+col] 
                    for i in range(arr.shape[0]-row+1) 
                    for j in range(arr.shape[1]-col+1)
            ]
            for submatrix in submatrices:
                if submatrix.size == 49:
                    counter += 1
    return counter
