
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        j = i
        while j < len(circular_list) and product <= -779:
            product *= circular_list[j]
            j += 1
        if product == -779:
            sublists.append(circular_list[i:j])
    return sublists
