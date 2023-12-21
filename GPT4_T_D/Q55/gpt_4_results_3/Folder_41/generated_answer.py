
def lists_with_product_equal_n(circular_list):
    results = []
    length = len(circular_list)

    long_list = circular_list * 2
    
    for start_index in range(length):
        sublist_start, sublist_end = start_index, start_index + 1
        
        while sublist_end <= start_index + length:
            sublist = long_list[sublist_start:sublist_end]
            product = 1
            
            for integer in sublist:
                product *= integer
            
            if product == -20:
                results.append(sublist)
                
            sublist_end += 1
            
    return results
