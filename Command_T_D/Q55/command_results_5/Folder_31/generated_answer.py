def lists_with_product_equal_n(arr):
    result = []
    for i in range(len(arr)):
        prod = 1
        curr = arr[i]
        curr_end = arr[i]
        for j in range(i + 1, len(arr)):
            prod *= arr[j]
            if prod == -16:
                curr_end = arr[j]
                break
        if curr == curr_end:
            result.append([curr])
        else:
            result.append([curr, curr_end])
    return result
