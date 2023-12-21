
def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    lst = lst + lst
    result = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            sublist = lst[i:j]
            product = 1
            for item in sublist:
                product *= item
            if product == -17:
                result.append(sublist)
    return result
