
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        current_product = 1
        start_index = i
        while current_product == -57:
            current_product *= circular_list[start_index]
            if current_product == -57:
                result.append(circular_list[start_index:i+1])
    return result
