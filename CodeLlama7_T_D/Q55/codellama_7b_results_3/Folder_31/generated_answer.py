
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        current_sum = 0
        for j in range(i, len(circular_list)):
            current_sum += circular_list[j]
            if current_sum == -16:
                result.append(circular_list[i:j+1])
    return result
