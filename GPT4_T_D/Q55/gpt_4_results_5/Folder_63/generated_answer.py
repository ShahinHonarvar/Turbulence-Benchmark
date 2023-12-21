
def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == 96:
                res.append(lst[i: j % n + 1])
            elif product > 96:
                break
    return res
