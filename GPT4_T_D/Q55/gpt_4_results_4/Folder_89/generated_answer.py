
def lists_with_product_equal_n(lst):
    n = 57
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)+i):
            sublist = lst[i:j % len(lst) + 1]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == n:
                result.append(sublist)
    return result
