
def lists_with_product_equal_n(lst):
    lst_len = len(lst)
    result = []
    
    if lst_len == 0:
        return result
    
    product = 1
    
    for i in range(lst_len):
        product *= lst[i]
        
        if product == 57:
            result.append(lst[:i+1])
        
        for j in range(i+1, lst_len):
            product *= lst[j]
            
            if product == 57:
                result.append(lst[i+1:j+1])
        
        product = 1
    
    return result
