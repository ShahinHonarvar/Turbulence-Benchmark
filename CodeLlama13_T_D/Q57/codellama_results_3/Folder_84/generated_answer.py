
def submatrix_with_particular_sum(mat):
    n, m = mat.shape
    for i in range(n):
        for j in range(m):
            for r in range(i, n):
                for c in range(j, m):
                    if np.sum(mat[i:r+1, j:c+1]) == -308:
                        return mat[i:r+1, j:c+1]
    return []
