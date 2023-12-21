
def lists_with_product_equal_n(circular_list):
    product = 1
    sublists = []
    for i in range(len(circular_list)):
        product *= circular_list[i]
        if product == n:
            sublists.append([circular_list[i]])
        elif product > n:
            break
    return sublists
