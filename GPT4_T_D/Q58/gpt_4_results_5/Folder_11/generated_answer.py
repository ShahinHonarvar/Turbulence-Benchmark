
import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    shape = mat.shape
    for width in range(shape[1]+1):
        for height in range(shape[0]+1):
            if (width * height == 38):
                for i in range(shape[0]-height+1):
                    for j in range(shape[1]-width+1):
                        count += 1
    return count
