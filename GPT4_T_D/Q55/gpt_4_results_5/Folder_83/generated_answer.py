
def lists_with_product_equal_n(lst):
    length = len(lst)
    result = []

    for i in range(length):
        for j in range(i, i+length):
            sublist = lst[i:j] if j<=length else lst[i:] + lst[:j-length]
            product = 1
            for val in sublist:
                product *= val
            if product == -57:
                result.append(sublist)

    return result
