
def submatrix_with_particular_sum(mat):
    n, m = len(mat), len(mat[0])
    for i in range(n):
        for j in range(m):
            if sum(mat[i][j:]) == -81:
                return [[mat[k][l] for l in range(j, m)] for k in range(i, n)]
    return []
