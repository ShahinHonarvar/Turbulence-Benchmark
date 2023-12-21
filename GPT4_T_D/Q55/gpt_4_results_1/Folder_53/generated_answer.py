
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for length in range(1, size + 1):
        for start in range(size):
            sublist = lst[start:start + length]
            if len(sublist) < length:
                sublist += lst[:(length - len(sublist))]
            product = 1
            for num in sublist:
                product *= num
            if product == -87:
                result.append(sublist)
    return result
