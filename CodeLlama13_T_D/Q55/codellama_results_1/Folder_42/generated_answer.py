
def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        j = i
        while j < len(circular_list) and product <= n:
            sublist.append(circular_list[j])
            product *= circular_list[j]
            j += 1
        if product == n:
            result.append(sublist)
    return result
