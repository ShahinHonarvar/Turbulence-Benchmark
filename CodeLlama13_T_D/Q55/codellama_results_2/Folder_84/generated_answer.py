
def lists_with_product_equal_n(circular_list):
    product = 1
    result = []
    for i in range(len(circular_list)):
        product *= circular_list[i]
        if product == -906:
            result.append([circular_list[i]])
        elif product > -906:
            break
    return result
