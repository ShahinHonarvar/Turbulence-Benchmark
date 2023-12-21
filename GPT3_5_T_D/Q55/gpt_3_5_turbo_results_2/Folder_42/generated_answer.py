
def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    for i in range(size):
        product = 1
        for j in range(size):
            index = (i + j) % size
            product *= circular_list[index]
            if product == 25:
                sublist = circular_list[i: (i + j + 1) % size]
                if sublist not in sublists:
                    sublists.append(sublist)
    return sublists
