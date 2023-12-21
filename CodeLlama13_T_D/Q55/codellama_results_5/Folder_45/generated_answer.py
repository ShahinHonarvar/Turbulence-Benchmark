
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        j = i
        while product != -5:
            product *= circular_list[j]
            sublist.append(circular_list[j])
            j += 1
            if j == len(circular_list):
                j = 0
        result.append(sublist)
    return result
