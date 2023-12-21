
def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        prod = 1
        sublist = []
        j = i
        while prod <= n:
            sublist.append(circular_list[j])
            prod *= circular_list[j]
            j += 1
            if j == len(circular_list):
                j = 0
        if prod == n:
            result.append(sublist)
    return result
