
def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)

    for i in range(size):
        product = 1
        sublist = []
        
        for j in range(i, i + size):
            product *= circular_list[j % size]
            sublist.append(circular_list[j % size])
            
            if product == -57:
                sublists.append(sublist[:])
                break
                    
    return sublists
