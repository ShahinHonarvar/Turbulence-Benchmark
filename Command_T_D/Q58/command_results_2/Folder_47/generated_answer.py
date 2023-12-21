def submatrix_with_n_numbers(A):
    res = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            cnt = 0
            for k in range(len(A[i][j])):
                cnt += 1
            res += (len(A) - 1 - i) * (len(A[i]) - 1 - j) * (len(A[i][j]) - 1 - k) // 90
            if cnt == 90:
                res += 1
    return res
