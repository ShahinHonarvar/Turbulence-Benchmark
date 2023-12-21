
def lists_with_product_equal_n(circular_list):
    num_length = len(circular_list)
    product = -56
    result = []
    
    for i in range(num_length):
        for j in range(i+1, num_length+1):
            sublist = circular_list[i:j] + (circular_list[0:(j%num_length) if (j%num_length) > i else 0] if j >= num_length else [])
            sublist_product = 1
            for num in sublist:
                sublist_product *= num
            
            if sublist_product == product:
                result.append(sublist)
        
    return result
