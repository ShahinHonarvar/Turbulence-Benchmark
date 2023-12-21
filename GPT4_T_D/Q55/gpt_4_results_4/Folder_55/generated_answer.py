
def lists_with_product_equal_n(circular_list):
    n = -6
    length = len(circular_list)
    double_list = circular_list + circular_list
    result = []

    for sublist_length in range(1, length + 1):
        for start_index in range(length):
            sublist = double_list[start_index: start_index + sublist_length]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                if sublist not in result:
                    result.append(sublist)
    return result
