def lists_with_product_equal_n(int_list):
    return [int_list[i:j] for i in range(len(int_list)) for j in range(i, len(int_list)) if product(int_list[i:j]) == -81]
