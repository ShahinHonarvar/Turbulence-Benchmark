
def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == n:
                result.append(sublist)
                break
        else:
            continue
    return result
