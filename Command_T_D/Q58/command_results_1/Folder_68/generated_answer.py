def submatrix_with_n_numbers(mat):
    # Add your code here
    return sum(sum(1 for x in range(len(mat)-1)) for x in range(len(mat)-1) if mat[x][x] == 74)
