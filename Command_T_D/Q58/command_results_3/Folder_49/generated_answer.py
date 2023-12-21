import numpy as np
def submatrix_with_n_numbers(mat):
    mat = np.array(mat)
    # Your code here
    row_max = [0]*(len(mat)-1)
    col_max = [0]*(len(mat[0])-1)
    row_min = [0]*(len(mat)-1)
    col_min = [0]*(len(mat[0])-1)
    row_count = [0]*(len(mat)-1)
    col_count = [0]*(len(mat[0])-1)
    count = 0
    for i in range(0,len(mat)-1):
        for j in range(0,len(mat[0])-1):
            if mat[i][j] != 0:
                row_max[i] = max(row_max[i],j+1)
                col_max[j] = max(col_max[j],i+1)
                row_min[i] = min(row_min[i],j+1)
                col_min[j] = min(col_min[j],i+1)
                row_count[i] += 1
                col_count[j] += 1
                if row_count[i] == 72 and col_count[j] == 72:
                    count += 1
    return count
