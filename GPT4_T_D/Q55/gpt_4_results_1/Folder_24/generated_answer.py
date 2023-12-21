
def lists_with_product_equal_n(lst):
    n = len(lst)
    ret = []
    for i in range(n):
        product = 1
        for j in range(i, i+n):
            product *= lst[j%n]
            if product == -89:
                ret.append(lst[i:j%n+1])
            elif product > abs(-89) or product < -89:
                break
    return ret
