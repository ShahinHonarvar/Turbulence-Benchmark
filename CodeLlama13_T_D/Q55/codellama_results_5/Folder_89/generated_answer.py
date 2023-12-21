
def lists_with_product_equal_n(circular_list):
    product = 1
    sublists = []
    for i in range(len(circular_list)):
        product *= circular_list[i]
        if product == n:
            sublists.append([])
        elif product > n:
            sublists[-1].append(circular_list[i-1])
    return sublists
