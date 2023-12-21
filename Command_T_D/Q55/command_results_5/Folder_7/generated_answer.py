def lists_with_product_equal_n(int_list):
    return [[int_list[i] for i in range(len(int_list)) if int_list[i] == n]] for n in range(1, 538) if n == int_list[0] * n == int_list[-1]
