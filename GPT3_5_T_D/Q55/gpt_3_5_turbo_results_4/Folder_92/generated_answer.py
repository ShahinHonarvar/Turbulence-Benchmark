
def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)
    product = 1

    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= circular_list[j % size]
            if product == 5:
                result.append(circular_list[i:j % size + 1])

    return result
