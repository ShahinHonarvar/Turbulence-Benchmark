
def lists_with_product_equal_n(circular_list):
    result = []
    length = len(circular_list)
    
    for i in range(length):
        product = 1
        sublist = []
        
        for j in range(length):
            index = (i + j) % length
            sublist.append(circular_list[index])
            product *= circular_list[index]
            
            if product == -33:
                result.append(sublist[:])
        
    return result
