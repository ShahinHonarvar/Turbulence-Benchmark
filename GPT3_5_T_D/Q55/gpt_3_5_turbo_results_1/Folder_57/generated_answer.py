
def lists_with_product_equal_n(circular_list):
    result = []
    length = len(circular_list)
    for i in range(length):
        temp_product = 1
        for j in range(length):
            temp_product *= circular_list[(i+j) % length]
            if temp_product == -75:
                result.append(circular_list[i:i+j+1])
    return result
