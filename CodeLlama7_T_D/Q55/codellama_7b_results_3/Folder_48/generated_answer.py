
def lists_with_product_equal_n(circular_list):
    result = []
    # loop through the list and find all contiguous sublists with product equal to n
    for i in range(len(circular_list)):
        current_sum = 1
        for j in range(i, len(circular_list)):
            current_sum *= circular_list[j]
            if current_sum == n:
                result.append(circular_list[i:j+1])
    return result
