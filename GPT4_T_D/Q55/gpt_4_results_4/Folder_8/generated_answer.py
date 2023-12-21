
def lists_with_product_equal_n(lst):
    n = len(lst)
    ret = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = lst[i:j] if j > i else lst[i:] + lst[:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -41:
                ret.append(sublist)
    return ret
