
def lists_with_product_equal_n(lst):
    n = len(lst)
    if n==0: return []
    lst = lst + lst
    res = []
    for L in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i+L]
            product = 1
            for num in sublist:
                product *= num
            if product==-8:
                res.append(sublist)
    dedup_res = [list(x) for x in set(tuple(x) for x in res)]
    return dedup_res
