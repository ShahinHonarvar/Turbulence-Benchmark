
def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    target_product = 90

    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= circular_list[j % size]
            if product == target_product:
                sublists.append(circular_list[i: j % size + 1])

    return sublists
