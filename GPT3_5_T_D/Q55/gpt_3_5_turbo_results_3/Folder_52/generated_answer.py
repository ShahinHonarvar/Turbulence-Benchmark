
def lists_with_product_equal_n(lst):
    if not lst:
        return []
    
    n = len(lst)
    sublists = []
    
    for i in range(n):
        for j in range(i, n + i):
            product = 1
            sublist = []
            
            for k in range(i, j + 1):
                product *= lst[k % n]
                sublist.append(lst[k % n])
                
            if product == 37:
                sublists.append(sublist)
    
    return sublists
