
def lists_with_product_equal_n(circular_list):
    result = []
    length = len(circular_list)
    product = 1
    start = 0
    
    for i in range(length*2):
        if product == 8:
            result.append(circular_list[start:i])
        
        while product >= 8 and start < i-1:
            product = product / circular_list[start]
            start += 1
        
        while product < 8 and i < length*2:
            product = product * circular_list[i % length]
            i += 1
    
    return result
