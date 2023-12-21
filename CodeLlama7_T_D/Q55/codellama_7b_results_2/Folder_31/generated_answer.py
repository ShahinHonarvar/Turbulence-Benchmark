
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        current_index = i
        while product != -16:
            product *= circular_list[current_index]
            current_index = (current_index + 1) % len(circular_list)
        if product == -16:
            sublists.append(circular_list[i:current_index])
    return sublists
