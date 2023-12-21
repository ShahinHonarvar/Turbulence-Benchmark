
def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)

    for i in range(size):
        product = 1
        for j in range(size):
            index = (i + j) % size
            product *= circular_list[index]

            if product == -41:
                result.append(circular_list[i:index + 1])

    return result
