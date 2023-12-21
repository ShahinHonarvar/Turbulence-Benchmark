
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, len(circular_list) + i):
            product *= circular_list[j % len(circular_list)]
            sublist.append(circular_list[j % len(circular_list)])
            if product == 13:
                result.append(sublist)
                break
        else:
            continue
    return result
