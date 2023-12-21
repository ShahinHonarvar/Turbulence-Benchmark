def submatrix_with_particular_sum(arr):
    return [sub for i in range(len(arr)-1) for j in range(len(arr)-1) for sub in [[arr[i][j]] + [arr[i][j+1]:i+1] + [[arr[i+1][j]] + [arr[i+1][j+1]:i+1] + [[arr[i+2][j]] + [arr[i+2][j+1]:i+1]] if sum(sub) == 56]
