
def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    result = []

    for i in range(size):
        product = 1
    
        for j in range(size):
            idx = (i + j) % size
            product *= circular_list[idx]
        
            if product == 32:
                sub_list = circular_list[i:idx+1]
                result.append(sub_list)
        
            elif product > 32:
                break
    
    return result
