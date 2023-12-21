
def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    product = 1
    
    for i in range(n):
        product *= circular_list[i]
        if product == -95:
            result.append(circular_list[:i+1])
    
    for i in range(n):
        product /= circular_list[i]
        if product == -95:
            result.append(circular_list[i+1:] + circular_list[:i+1])
    
    return result
