
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = lst[i:j] + (lst[:i-j+n] if j>i else [])
            prod = 1
            for x in sublist:
                prod *= x
            if prod == 415:
                result.append(sublist)
    return result
