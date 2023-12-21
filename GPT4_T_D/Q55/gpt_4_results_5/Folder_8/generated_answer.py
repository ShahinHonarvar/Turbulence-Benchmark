
def lists_with_product_equal_n(lst):
    size = len(lst)
    res = []
    lst = lst + lst
    
    for i in range(size):
        for j in range(i+1, size+1):
            sub = lst[i:j]
            product = 1
            for x in sub:
                product *= x
            if product == -41:
                res.append(sub)
                
    return res
