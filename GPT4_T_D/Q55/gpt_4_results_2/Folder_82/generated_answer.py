
def lists_with_product_equal_n(lst):
    import numpy as np
    res = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sublist = lst[i:j]
            if j==len(lst) and i>0:
                sublist.append(lst[0])
            if np.prod(sublist) == 8:
                res.append(sublist)
    return res
