
def lists_with_product_equal_n(arr):
    result = []
    for i in range(len(arr)):
        product = 1
        for j in range(i, i + len(arr)):
            product *= arr[j % len(arr)]
            if product == -76:
                result.append(arr[i:j + 1])
    return result
