
def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)
    for i in range(size):
        sublist = []
        product = 1
        for j in range(i, size + i):
            product *= circular_list[j % size]
            sublist.append(circular_list[j % size])
            if product == 415:
                result.append(sublist)
    return result
