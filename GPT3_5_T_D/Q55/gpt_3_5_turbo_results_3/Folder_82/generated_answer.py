
def lists_with_product_equal_n(circular_list):
    sublists = []
    
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        
        for j in range(i, len(circular_list)+i):
            product *= circular_list[j % len(circular_list)]
            sublist.append(circular_list[j % len(circular_list)])
            
            if product == 8:
                sublists.append(sublist)
                break
    
    return sublists
