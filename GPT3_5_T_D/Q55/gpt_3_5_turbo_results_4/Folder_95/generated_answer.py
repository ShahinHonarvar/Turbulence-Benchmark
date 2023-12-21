
def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    
    for i in range(size):
        for j in range(i, size):
            sublist = lst[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == 28:
                sublists.append(sublist)
    
    return sublists
