def lists_with_product_equal_n(arr):
    res = []
    for n in range(1,len(arr)):
        for j in range(n):
            if arr[j] == arr[n]:
                res += [[arr[j]] + [arr[j+1]]
    return res
