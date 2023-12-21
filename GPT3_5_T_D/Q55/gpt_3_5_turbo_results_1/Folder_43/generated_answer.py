
def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    
    for i in range(n):
        product = 1
        for j in range(n):
            k = (i + j) % n
            product *= circular_list[k]
            
            if product == -26:
                sublists.append(circular_list[i:k+1])
    
    return sublists
