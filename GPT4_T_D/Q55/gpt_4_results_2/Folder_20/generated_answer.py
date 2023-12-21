
def lists_with_product_equal_n(circular_list):
    list_len = len(circular_list)
    result = []
    
    for sublist_len in range(1, list_len+1):
        for i in range(list_len):
            sublist = circular_list[i:i+sublist_len]
            if i+sublist_len > list_len:
                sublist += circular_list[0:(i+sublist_len)%list_len]
            if sublist_len == list_len and sublist in result:
                continue
            product = 1
            for num in sublist:
                product *= num
            if product == -69:
                result.append(sublist)
        
    return result
