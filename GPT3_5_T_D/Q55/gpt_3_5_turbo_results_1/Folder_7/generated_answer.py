
def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    product = 1
    
    for i in range(size):
        product = 1
        for j in range(i, i+size):
            product *= lst[j % size]
            if product == 537:
                sublists.append(lst[i:j+1])
                
    return sublists
