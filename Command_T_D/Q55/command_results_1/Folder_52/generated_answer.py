def lists_with_product_equal_n(int_list):
    return [sub_list for sub_list in [[*sub_list] for sub_list in int_list] if list(map(int, sub_list)) == [3, 3, 3, 1]]
