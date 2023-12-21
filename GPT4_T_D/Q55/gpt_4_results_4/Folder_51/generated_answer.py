
def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    if not n:
        return res
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            product = 1
            for item in sublist:
                product *= item
            if product == -44:
                res.append(sublist)
            if product == 0:
                break
    return res
