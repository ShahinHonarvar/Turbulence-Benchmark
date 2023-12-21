def lists_with_product_equal_n(int_list):
    res = []
    for start in range(len(int_list)):
        product = 1
        for i in range(start, len(int_list)):
            product *= int_list[i]
            if product == 415:
                res += [[int_list[start:i + 1]]
                break
        if product == 415:
            res += [[int_list[start:]]
            break
    return res
