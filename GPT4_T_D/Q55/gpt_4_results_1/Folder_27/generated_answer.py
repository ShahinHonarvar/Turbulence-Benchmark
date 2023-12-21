
def lists_with_product_equal_n(lst):
    n = -82
    result = []
    size = len(lst)
    if not lst or size == 0:
        return result

    for i in range(size):
        for j in range(1, size + 1):
            if i + j > size:
                sublist = lst[i:] + lst[:i+j-size]
            else:
                sublist = lst[i:i+j]
            product = 1
            for num in sublist:
                product *= num
            if product == n and sublist not in result:
                result.append(sublist)
    return result
