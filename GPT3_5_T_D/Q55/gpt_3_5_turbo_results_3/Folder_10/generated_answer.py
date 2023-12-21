
def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    sublists = []

    for i in range(size):
        sublist = []
        product = 1
        for j in range(size):
            k = (i + j) % size
            sublist.append(circular_list[k])
            product *= circular_list[k]
            if product == -93:
                sublists.append(sublist[:])
    return sublists
