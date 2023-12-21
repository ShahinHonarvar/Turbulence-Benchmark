def submatrix_with_particular_sum(arr):
    result = []
    for i in range(len(arr)):
        for j in range(len(arr[0])), 0, -1):
            curr_sum = 0
            curr_idx = j
            for k in range(i, len(arr)):
                curr_sum += arr[k][curr_idx]
                curr_idx -= 1
            if curr_sum == -86:
                result.append(arr[i][:j] + arr[i][j+1:])
    return result
