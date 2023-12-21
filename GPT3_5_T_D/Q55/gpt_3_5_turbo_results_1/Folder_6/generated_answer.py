
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i+n):
            product *= circular_list[j % n]
            sublist.append(circular_list[j % n])
            if product == 42:
                result.append(sublist)
    return result
