
def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    
    for i in range(size):
        product = 1
        sublist = []
        for j in range(size):
            index = (i + j) % size
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == 37:
                sublists.append(sublist)
                break
    
    return sublists
