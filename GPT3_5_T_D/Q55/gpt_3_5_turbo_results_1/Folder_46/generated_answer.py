
def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j + 1):
                product *= arr[k % n]
            if product == 53:
                result.append(arr[i:j+1])
    return result
