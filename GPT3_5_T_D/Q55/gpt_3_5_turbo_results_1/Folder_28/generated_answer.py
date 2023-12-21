
def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    product = 1
    start = 0
    
    for end in range(size):
        product *= circular_list[end]
        
        while product > 85 and start <= end:
            product /= circular_list[start]
            start += 1
            
        if product == 85:
            sublists.append(circular_list[start:end + 1])
            
    return sublists
