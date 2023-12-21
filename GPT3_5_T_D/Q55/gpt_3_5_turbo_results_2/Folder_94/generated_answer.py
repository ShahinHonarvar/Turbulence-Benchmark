
def lists_with_product_equal_n(circular_list):
    sublists = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= circular_list[j % length]
            if product == -30:
                sublists.append(circular_list[i:j % length + 1])
    return sublists
