
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        sublist = []
        product = 1
        for j in range(len(circular_list)):
            index = (i + j) % len(circular_list)
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == 36:
                result.append(sublist[:])
    return result
