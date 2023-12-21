
def lists_with_product_equal_n(circular_list):
    result = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        for j in range(0, length):
            index = (i + j) % length
            product *= circular_list[index]
            if product == 40:
                result.append(circular_list[i:index+1])
    return result
