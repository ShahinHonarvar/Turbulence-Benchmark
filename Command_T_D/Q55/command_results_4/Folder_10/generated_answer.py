def lists_with_product_equal_n(int_list):
    return [[i for i in int_list[i:j]] for i in range(len(int_list)) for j in range(i, len(int_list)) if int_list[i] * (j - i) == -93]
