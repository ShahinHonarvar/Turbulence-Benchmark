
def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        temp_product = 1
        for j in range(n):
            temp_product *= circular_list[(i+j) % n]
            if temp_product == -5:
                result.append(circular_list[i:i+j+1])
    return result
