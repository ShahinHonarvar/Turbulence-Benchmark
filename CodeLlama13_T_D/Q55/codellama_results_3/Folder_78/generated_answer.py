
def lists_with_product_equal_n(circular_list, n):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        sublist = [circular_list[i]]
        j = (i + 1) % len(circular_list)
        while product < n:
            product *= circular_list[j]
            sublist.append(circular_list[j])
            j = (j + 1) % len(circular_list)
        if product == n:
            sublists.append(sublist)
    return sublists
