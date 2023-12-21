
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    target = 47
    
    for i in range(n):
        product = 1
        sub_lst = []
        
        for j in range(i, i + n):
            idx = j % n
            product *= lst[idx]
            sub_lst.append(lst[idx])
            
            if product == target:
                result.append(sub_lst)
    
    return result
