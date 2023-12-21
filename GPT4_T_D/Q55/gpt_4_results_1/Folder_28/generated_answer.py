
def lists_with_product_equal_n(circular_list):
    list_length = len(circular_list)
    circular_list = circular_list * 2
    final_list = []
    for window_size in range(1, list_length + 1):
        for start_index in range(list_length):
            sublist = circular_list[start_index:start_index + window_size]
            product = 1
            for num in sublist:
                product *= num
            if product == 85:
                final_list.append(sublist)
    return final_list
