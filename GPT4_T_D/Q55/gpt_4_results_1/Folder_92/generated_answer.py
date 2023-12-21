
def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length + 1):
            sublist = lst[i:j] if j != length else lst[i:] + lst[:1]
            product = 1
            for num in sublist:
                product *= num
            if product == 5:
                result.append(sublist)
    return result
