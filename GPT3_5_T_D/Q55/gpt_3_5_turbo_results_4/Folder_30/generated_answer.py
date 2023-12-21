
def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)

    for i in range(n):
        product = 1
        for j in range(i, i+n):
            product *= circular_list[j % n]
            if product == 99:
                result.append(circular_list[i:j % n])

    return result
