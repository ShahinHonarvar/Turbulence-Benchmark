
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        sublist = []
        for j in range(i, i + size):
            index = j % size
            product *= lst[index]
            sublist.append(lst[index])
            if product == 415:
                result.append(sublist)
    return result
