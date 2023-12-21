
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublist = lst[i:i+1]
        product = 1
        for j in range(len(sublist)):
            product *= sublist[j]
        if product == n:
            result.append(sublist)
    return result
