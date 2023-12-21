
def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    
    for i in range(size):
        product = 1
        
        for j in range(i, size+i):
            product *= lst[j % size]
            
            if product == 78:
                sublists.append(lst[i:j % size + 1])
                
    return sublists
