
def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == -72:
                res.append(lst[i:(j % n)+1])
            if product == 0:
                break
    return res
