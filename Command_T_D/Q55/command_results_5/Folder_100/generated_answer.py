def lists_with_product_equal_n(num_list):
    lists = []
    for n in range(1, len(num_list) + 1):
        if num_list[0] * n == 48:
            lists += [[num_list[0]] + num_list[1:]]
            break
    return lists
