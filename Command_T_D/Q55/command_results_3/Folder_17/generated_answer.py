def lists_with_product_equal_n(int_list):
    result = []
    for start in range(len(int_list)):
        tail = [int_list[start]]
        for n in range(1, len(int_list)):
            product = 1
            for i in range(len(tail)):
                product *= tail[i]
            if product == 18:
                result.append(tail)
                tail = []
    return result
