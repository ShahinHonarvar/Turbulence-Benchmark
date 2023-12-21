def submatrix_with_particular_sum(A):
    res = []
    for i in range(len(A) - 1):
        for j in range(len(A[0]) - 1):
            if A[i][j] == 40:
                res += [[A[i][j]] + [[A[i][j + 1]] * (len(A) - i - 1)] + [[A[i + 1][j]] * (len(A[0]) - j - 1)]
    return res
