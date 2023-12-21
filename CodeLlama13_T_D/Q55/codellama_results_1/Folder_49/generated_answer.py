
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == -61:
                result.append(sublist)
    return result
