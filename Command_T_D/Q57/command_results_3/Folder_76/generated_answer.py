def submatrix_with_particular_sum(A):
    def dfs(A, x, y, current_sum):
        nonlocal res
        if current_sum == -255:
            res.append((A[x][y], (x, y)))
        for i in range(x - 1, -1, -1):
            for j in range(y - 1, -1, -1):
                dfs(A, i, j, current_sum + A[x][y])
    A = np.array(A)
    res = []
    dfs(A, 0, 0, 0)
    return res
