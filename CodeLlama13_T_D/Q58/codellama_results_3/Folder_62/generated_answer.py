
def submatrix_with_n_numbers(arr):
    n = 186
    rows, cols = len(arr), len(arr[0])
    count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            submat = arr[i:i+n,j:j+n]
            if np.all(submat == n):
                count += 1
    return count
