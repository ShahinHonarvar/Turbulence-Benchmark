
def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)
    product = 1
    for i in range(size):
        product *= circular_list[i]
        if product == -76:
            result.append(circular_list[:i + 1])
        for j in range(i + 1, size):
            product *= circular_list[j]
            if product == -76:
                result.append(circular_list[i + 1:j + 1])
    return result
