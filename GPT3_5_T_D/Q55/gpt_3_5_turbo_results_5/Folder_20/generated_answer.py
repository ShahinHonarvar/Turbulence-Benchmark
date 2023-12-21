
def lists_with_product_equal_n(lst):
    size = len(lst)
    sublists = []
    
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= lst[j % size]
            if product == -69:
                sublists.append(lst[i:i+j+1])
                
    return sublists
