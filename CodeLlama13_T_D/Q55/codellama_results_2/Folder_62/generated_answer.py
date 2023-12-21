
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(i+1, len(circular_list)):
            product = 1
            for k in range(i, j):
                product *= circular_list[k]
            if product == 100:
                result.append(circular_list[i:j])
    return result
