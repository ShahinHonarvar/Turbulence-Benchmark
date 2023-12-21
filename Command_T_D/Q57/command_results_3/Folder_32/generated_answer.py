def submatrix_with_particular_sum(arr):
    return [[*sub] for i in range(len(arr)) for j in range(len(arr[i])) for sub in zip(arr[i][:j] + arr[i][j+1:], arr[i+1][:j] + arr[i+1][j+1:]) if sum(sub) == 901]
