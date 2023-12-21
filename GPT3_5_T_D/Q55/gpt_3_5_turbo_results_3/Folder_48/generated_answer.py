
def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)

    for i in range(size):
        product = 1
        j = i
        
        while product < 990:
            product *= circular_list[j]
            sublists.append(circular_list[i:j+1])
            j = (j + 1) % size
        
        if product == 990:
            return sublists
    
    return []
