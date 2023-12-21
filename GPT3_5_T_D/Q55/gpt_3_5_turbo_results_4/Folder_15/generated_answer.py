
def lists_with_product_equal_n(lst):
    length = len(lst)
    res = []
    
    for i in range(length):
        prod = 1
        for j in range(i, i+length):
            prod *= lst[j % length]
            if prod == -7:
                res.append(lst[i:j+1])
    
    return res
