
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    result = []
    
    for i in range(length):
        sublist_product = 1
        
        for j in range(i, length + i):
            sublist_product *= circular_list[j % length]
            
            if sublist_product == -95:
                sub_list = circular_list[i:j % length + 1]
                result.append(sub_list)
    
    return result
