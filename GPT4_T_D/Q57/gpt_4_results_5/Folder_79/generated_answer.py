
import numpy as np

def submatrix_with_particular_sum(arr):
    elements = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for k in range(i+1, len(arr)+1):
                for l in range(j+1, len(arr[0])+1):
                    if np.sum(arr[i:k,j:l]) == -47:
                        elements.append(arr[i:k,j:l])
    return elements
