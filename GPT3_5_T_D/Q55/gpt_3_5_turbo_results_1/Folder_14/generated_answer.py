
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    product = lambda sublist: 1 if len(sublist) == 0 else sublist[0] * product(sublist[1:])
    for i in range(size):
        for j in range(i, size):
            if product(lst[i:j+1]) == -72:
                result.append(lst[i:j+1])
    return result
