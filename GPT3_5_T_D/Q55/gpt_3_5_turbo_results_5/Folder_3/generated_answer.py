
def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    for i in range(size):
        prod = 1
        for j in range(i, i+size):
            prod *= circular_list[j % size]
            if prod == -22:
                sublists.append(circular_list[i:j+1])
    return sublists
