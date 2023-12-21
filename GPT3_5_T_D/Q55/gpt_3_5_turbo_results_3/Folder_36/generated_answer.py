
def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    product = 1
    
    for i in range(n):
        for j in range(i, n):
            product *= circular_list[j]
            if product == 714:
                sublists.append(circular_list[i:j+1])
        product = 1
    
    return sublists
