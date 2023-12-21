
def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)
    
    for i in range(size):
        num = circular_list[i]
        if num == 1 or 36 % num != 0:
            continue
        
        product = num
        sublist = [num]
        j = i + 1
        
        while product != 36:
            if j == size:
                j = 0
            
            if size == 1:
                break
            
            next_num = circular_list[j]
            if next_num == 1 or 36 % next_num != 0:
                break
            
            sublist.append(next_num)
            product *= next_num
            j += 1
        
        if product == 36:
            result.append(sublist)
    
    return result
