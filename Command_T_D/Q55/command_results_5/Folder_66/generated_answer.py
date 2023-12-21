def lists_with_product_equal_n(arr):
    res = []
    for x in range(1, len(arr)):
        for y in range(1, x):
            if arr[x] * arr[y] == 78:
                res.append(list(range(x, y + 1)))
    return res
