
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        j = i
        while product <= 3 and j < len(circular_list):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            j += 1
        if product == 3:
            result.append(sublist)
    return result
