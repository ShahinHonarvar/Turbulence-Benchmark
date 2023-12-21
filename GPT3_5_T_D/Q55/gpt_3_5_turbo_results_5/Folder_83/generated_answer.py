
def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    
    for i in range(n):
        product = 1
        for j in range(i, n+i):
            product *= circular_list[j % n]
            if product == -57:
                sublists.append(circular_list[i:j+1])
    
    return sublists
