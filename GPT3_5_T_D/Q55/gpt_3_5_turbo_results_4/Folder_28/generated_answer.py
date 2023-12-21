
def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    
    for i in range(size):
        product = 1
        for j in range(size):
            if product * lst[j] == 85:
                sublists.append(lst[i:j+1])
            product *= lst[j]
    
    return sublists
