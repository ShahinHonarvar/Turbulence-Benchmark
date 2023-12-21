
import numpy as np

def sum_submat(mat):
    s = {}
    m, n = np.shape(mat)
    for x in range(m + 1):
        for y in range(n + 1):
            if x == 0 or y == 0:
                s[x, y] = 0
            else:
                s[x, y] = mat[x - 1][y - 1] + s[x, y - 1] + s[x - 1, y] - s[x - 1, y - 1]
    return s

def find_sum(sums, m, n, s):
    for size_x in range(1, m + 1):
        for size_y in range(1, n + 1):
            for x in range(size_x, m + 1):
                for y in range(size_y, n + 1):
                    if sums[x, y] - sums[x - size_x, y] - sums[x, y - size_y] + sums[x - size_x, y - size_y] == s:
                        yield(np.array(mat)[x - size_x:x, y - size_y:y])

def submatrix_with_particular_sum(mat):
    sums = sum_submat(mat)
    m, n = np.shape(mat)
    return list(find_sum(sums, m, n, 616))
