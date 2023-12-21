
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) - 1):
            product = 1
            for k in range(i, j + 1):
                product *= circular_list[k]
            if product == 851:
                result.append(circular_list[i:j+1])
    return result
