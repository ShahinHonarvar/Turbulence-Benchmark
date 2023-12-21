
def lists_with_product_equal_n(lst):
    def prod(x):
        p = 1
        for i in x:
            p *= i
        return p

    n = len(lst)
    res = []
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = lst[i:j] + (lst[:j-n] if j > n else [])
            if prod(sublist) == 33:
                res.append(sublist)
    return res
