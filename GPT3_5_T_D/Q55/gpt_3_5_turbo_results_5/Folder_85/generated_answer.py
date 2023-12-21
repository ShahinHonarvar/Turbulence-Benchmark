
def lists_with_product_equal_n(circular_list):
    sublist_product_equal_n = []
    size_of_list = len(circular_list)
    
    for i in range(size_of_list):
        sublist_product = 1
        sublist = []
        
        for j in range(i, i + size_of_list):
            sublist_product *= circular_list[j % size_of_list]
            sublist.append(circular_list[j % size_of_list])
            
            if sublist_product == -97:
                sublist_product_equal_n.append(sublist.copy())
    
    return sublist_product_equal_n
