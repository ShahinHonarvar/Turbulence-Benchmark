
def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)
    for i in range(size):
        product = 1
        for j in range(size):
            product *= circular_list[(i+j) % size]
            if product == -30:
                result.append(circular_list[i:(i+j+1) % size])
    return result
