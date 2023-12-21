def lists_with_product_equal_n(num_list):
    result = []
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            product = num_list[i] * num_list[j]
            if product == 851:
                result += [[num_list[i], num_list[j]]
    return result
