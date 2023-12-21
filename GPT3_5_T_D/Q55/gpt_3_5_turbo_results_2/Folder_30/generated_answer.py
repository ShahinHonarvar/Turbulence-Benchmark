
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        for j in range(i, size):
            sublist = lst[i:j+1]
            if sublist and math.prod(sublist) == 99:
                result.append(sublist)
    return result
