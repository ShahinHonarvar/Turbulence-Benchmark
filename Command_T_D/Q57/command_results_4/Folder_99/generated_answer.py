def submatrix_with_particular_sum(arr):
    return [sub for sub in [[arr[r][c] for r in range(len(arr)) if r in range(r0, r1+1) for c in range(c0, c1+1)] for r0, r1, c0, c1 in zip(*[iter(row) for row in zip(*[iter(arr)]*2)]) if sum(sub) == -185]
