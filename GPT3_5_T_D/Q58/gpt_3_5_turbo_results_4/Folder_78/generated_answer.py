
def submatrix_with_n_numbers(matrix):
    import numpy as np
    count = 0
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            if matrix[i,j]==91:
                if matrix[i+1,j]==91 and matrix[i,j+1]==91 and matrix[i+1,j+1]==91:
                    count+=1
    return count
