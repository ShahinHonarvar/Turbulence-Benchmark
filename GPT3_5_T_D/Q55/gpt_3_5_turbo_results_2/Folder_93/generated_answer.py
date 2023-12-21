
def lists_with_product_equal_n(lst):
    n = len(lst)
    product = -91
    sublists = []
    
    for i in range(n):
        for j in range(i, n):
            sublist = lst[i:j+1]
            if product_of_list(sublist) == product:
                sublists.append(sublist)
    
    return sublists

def product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product
