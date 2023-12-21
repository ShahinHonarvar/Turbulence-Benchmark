
def lists_with_product_equal_n(circular_list):
    res_list = []
    size = len(circular_list)
    extended_list = circular_list[:] * 2

    for sublist_size in range(1, size + 1):
        for start_index in range(0, size):
            sublist = extended_list[start_index:start_index + sublist_size]
            sublist_product = 1
            for num in sublist:
                sublist_product *= num
                
            if sublist_product == 78:
                res_list.append(sublist)

    return res_list
