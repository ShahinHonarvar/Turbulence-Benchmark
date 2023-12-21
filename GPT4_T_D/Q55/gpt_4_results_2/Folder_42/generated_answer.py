
def lists_with_product_equal_n(lst):
    size = len(lst)
    result = []
    for i in range(size):
        product = 1
        sublist = []
        for j in range(i, i+size):
            product *= lst[j%size]
            sublist.append(lst[j%size])
            if product == 25:
                result.append(list(sublist))
            elif product > 25:
                break
    return result
