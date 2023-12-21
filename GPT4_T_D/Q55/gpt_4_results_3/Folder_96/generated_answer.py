
def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)

    for i in range(n):
        for j in range(i+1, n+1):
            sublist = lst[i:j]
            if i+1 > j:
                sublist += lst[:j]
            if len(sublist) > 0 and (0 in sublist):
                res.append(sublist)
    return res
