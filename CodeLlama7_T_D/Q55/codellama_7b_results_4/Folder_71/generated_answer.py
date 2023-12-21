
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == 47:
                sublist = lst[i:j+1]
                result.append(sublist)
    return result
