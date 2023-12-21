
def lists_with_product_equal_n(lst):
    if not lst:
        return []
    size = len(lst)
    lst = lst*2
    res = []
    for s in range(size):
        for e in range(s+1, s+size+1):
            sublist = lst[s:e]
            product = 1
            for num in sublist:
                product *= num
            if product == 32:
                while len(sublist) > size:
                    sublist.pop(0)
                res.append(sublist)
    return res
