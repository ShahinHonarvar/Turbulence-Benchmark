
def lists_with_product_equal_n(circular_list):
    result = []
    
    if len(circular_list) == 0:
        return result
    
    for i in range(len(circular_list)):
        product = 1
        
        for j in range(i, i + len(circular_list)):
            product *= circular_list[j % len(circular_list)]
            
            if product == -18:
                result.append(circular_list[i:j % len(circular_list) + 1])
    
    return result
