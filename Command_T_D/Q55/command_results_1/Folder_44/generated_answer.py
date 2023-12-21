def lists_with_product_equal_n(arr):
    if not arr:
        return []
    result = []
    for i in range(len(arr)):
        temp = []
        for j in range(i, len(arr)):
            temp.append(arr[j])
            if temp[-1] == 29:
                result.append(temp)
                temp = []
    return result
