def lists_with_product_equal_n(int_list):
    res = []
    current_prod = 1
    for i in range(len(int_list)):
        current_prod *= int_list[i]
        if current_prod == 4:
            res += [[int_list[i]]
            current_prod = 1
    return res
