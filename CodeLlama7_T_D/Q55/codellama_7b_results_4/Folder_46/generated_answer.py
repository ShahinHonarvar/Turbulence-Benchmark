
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = [circular_list[i]]
        while product < 53:
            i = (i + 1) % len(circular_list)
            product *= circular_list[i]
            sublist.append(circular_list[i])
        if product == 53:
            result.append(sublist)
    return result
