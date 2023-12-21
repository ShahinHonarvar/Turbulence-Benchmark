
def lists_with_product_equal_n(circular_list):
    sublists = []
    product = 1
    start_index = 0

    for i in range(len(circular_list)):
        product *= circular_list[i]
        while product > 54:
            product /= circular_list[start_index]
            start_index += 1
        if product == 54:
            sublists.append(circular_list[start_index:i+1])
    
    return sublists
