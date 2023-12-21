
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    circular_list += circular_list
    result = []

    for sub_length in range(1, length + 1):
        for i in range(length):
            sublist = circular_list[i:i + sub_length]
            product = 1
            for num in sublist:
                product *= num
            if product == -30:
                result.append(sublist)
    return result
