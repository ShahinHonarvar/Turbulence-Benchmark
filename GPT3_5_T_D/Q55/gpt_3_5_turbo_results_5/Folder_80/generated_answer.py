
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        temp_product = 1
        sublist = []
        for j in range(i, i + len(circular_list)):
            sublist.append(circular_list[j % len(circular_list)])
            temp_product *= circular_list[j % len(circular_list)]
            if temp_product == 43:
                result.append(sublist.copy())
    return result
