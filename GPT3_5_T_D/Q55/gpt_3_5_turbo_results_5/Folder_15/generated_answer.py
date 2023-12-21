
def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)
    for i in range(size):
        product = 1
        for j in range(size - 1):
            index = (i + j) % size
            product *= circular_list[index]
            if product == -7:
                sublist = circular_list[i:i + j + 1]
                result.append(sublist)
    return result
