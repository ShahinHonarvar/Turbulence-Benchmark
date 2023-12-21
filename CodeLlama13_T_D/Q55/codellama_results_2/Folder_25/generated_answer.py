
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, len(circular_list)):
            sublist.append(circular_list[j])
            product *= circular_list[j]
            if product == -32:
                result.append(sublist)
                break
    return result
