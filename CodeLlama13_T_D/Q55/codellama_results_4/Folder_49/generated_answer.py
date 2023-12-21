
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(i+1, len(circular_list)+1):
            product = 1
            for k in range(j-i):
                product *= circular_list[i+k]
            if product == -61:
                result.append(circular_list[i:j])
    return result
