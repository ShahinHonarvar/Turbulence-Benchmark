
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        sublist = []
        product = 1
        for j in range(i, i+n):
            index = j % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == -30:
                result.append(sublist.copy())
    return result
