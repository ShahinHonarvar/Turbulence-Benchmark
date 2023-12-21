
def lists_with_product_equal_n(circular_list):
    len_list = len(circular_list)
    circular_list.extend(circular_list)
    result = []

    for i in range(len_list):
        for j in range(i + 1, i + len_list + 1):
            sublist = circular_list[i:j]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == -69:
                result.append(sublist)
    return result
