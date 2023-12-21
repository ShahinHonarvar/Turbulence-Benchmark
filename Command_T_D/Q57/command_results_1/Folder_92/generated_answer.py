def submatrix_with_particular_sum(A):
    res = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            s = sum(A[i][j:j + 3])
            if s == -3:
                res += [[A[i][j]]]
            elif s == -2:
                res += [[A[i][j]]]
            elif s == -1:
                res += [[A[i][j]]]
    return res
