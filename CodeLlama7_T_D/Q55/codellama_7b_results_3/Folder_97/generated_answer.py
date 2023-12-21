
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        current_product = 1
        start = i

        while current_product != -938 and start < len(circular_list):
            current_product *= circular_list[start]
            start += 1

        if current_product == -938:
            sublists.append(circular_list[i:start])

    return sublists
