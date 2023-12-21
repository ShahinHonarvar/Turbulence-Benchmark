
def lists_with_product_equal_n(circular_list):
    result = []
    
    for i in range(len(circular_list)):
        sublist = []
        product = 1

        for j in range(i, len(circular_list) + i):
            k = j % len(circular_list)
            sublist.append(circular_list[k])
            product *= circular_list[k]

            if product == -8:
                result.append(sublist[:])
    
    return result
