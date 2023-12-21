
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            product = 1
            for k in range(i, j+1):
                product *= circular_list[k]
            if product == -51:
                sublists.append(circular_list[i:j+1])
    return sublists
