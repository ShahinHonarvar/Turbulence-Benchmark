
def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)
    int_product = 1

    if size == 0:
        return result

    for i in range(size):
        int_product = 1
        for j in range(i, size+i):
            int_product *= circular_list[j % size]
            if int_product == -81:
                result.append(circular_list[i:j % size + 1])
    return result
