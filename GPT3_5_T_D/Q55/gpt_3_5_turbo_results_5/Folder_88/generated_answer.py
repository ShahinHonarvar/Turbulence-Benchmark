
def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    product = -56
    sublists = []
    for i in range(size):
        sublist_product = 1
        for j in range(i, i+size):
            sublist_product *= circular_list[j % size]
            if sublist_product == product:
                sublists.append(circular_list[i:j+1])
    return sublists
