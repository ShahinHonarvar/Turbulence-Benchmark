
def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = lst[i:j]
            prod = 1
            for num in sub:
                prod *= num
            if prod == 48:
                res.append(sub)
        lst = lst[1:] + [lst[0]]
                
    return res
