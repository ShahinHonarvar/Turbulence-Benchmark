
def lists_with_product_equal_n(circular_list):
    product = 1
    sublists = []
    for i in range(len(circular_list)):
        if circular_list[i] == 0:
            continue
        product *= circular_list[i]
        if product % n != 0:
            continue
        sublists.append([])
        for j in range(i, len(circular_list)):
            if circular_list[j] == 0:
                break
            sublists[-1].append(circular_list[j])
    return sublists
