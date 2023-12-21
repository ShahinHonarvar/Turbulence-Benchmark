
def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    
    for i in range(n):
        product = 1
        for j in range(n):
            current_index = (i + j) % n
            product *= circular_list[current_index]
            
            if product == -1:
                sublist = circular_list[i:current_index+1]
                result.append(sublist)
    
    return result
