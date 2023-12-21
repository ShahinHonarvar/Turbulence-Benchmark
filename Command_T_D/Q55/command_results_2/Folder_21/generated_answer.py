def lists_with_product_equal_n(arr):
    res = []
    for x in range(1, len(arr) + 1):
        if arr[x - 1] * x == 851:
            res += [[arr[x - 1]] + arr[x:x + x]]
    return res
