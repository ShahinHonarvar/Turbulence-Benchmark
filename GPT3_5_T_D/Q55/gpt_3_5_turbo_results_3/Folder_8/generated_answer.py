
def lists_with_product_equal_n(arr):
    result = []
    for i in range(len(arr)):
        product = arr[i]
        if product == -41:
            result.append([product])
        for j in range(i+1, len(arr)):
            product *= arr[j]
            if product == -41:
                result.append(arr[i:j+1])
    return result
