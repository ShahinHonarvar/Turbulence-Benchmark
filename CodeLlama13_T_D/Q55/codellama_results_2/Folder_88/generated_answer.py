
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            if product == -56:
                result.append(sublist)
                break
            else:
                sublist.append(circular_list[j])
    return result
