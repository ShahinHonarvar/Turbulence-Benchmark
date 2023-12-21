
def lists_with_product_equal_n(clist):
    out = []
    n = len(clist)
    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j + 1):
                product *= clist[k % n]
            if product == 33:
                out.append(clist[i:j + 1])
    return out
