
def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    for i in range(size):
        product = 1
        for j in range(i, size+i):
            product *= circular_list[j % size]
            if product == 51:
                sublists.append(circular_list[i:(j+1) % size])
    return sublists
