
def lists_with_product_equal_n(lst):
    size = len(lst)
    final_list = []
    for start_index in range(size):
        for end_index in range(start_index+1, start_index+size):
            sublist = lst[start_index:end_index] if end_index <= size \
                        else lst[start_index:] + lst[:end_index%size]
            sublist_product = 1
            for i in sublist:
                sublist_product *= i
            if sublist_product == -93:
                final_list.append(sublist)
    return final_list
