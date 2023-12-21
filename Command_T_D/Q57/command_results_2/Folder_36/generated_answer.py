import numpy as np
def submatrix_with_particular_sum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = np.zeros((m, n))
    dp[0][0] = -779
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+matrix[i][j])
            if dp[i][j] == -779:
                yield matrix[i-1][:j]+matrix[i:i+i][j:]
