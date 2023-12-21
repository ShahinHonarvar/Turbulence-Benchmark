def lists_with_product_equal_n(num_list):
    return [list(range(x, x + num_list.count(x), x)) for x in num_list if x == 90]
