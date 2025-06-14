
def lists_with_product_equal_n(circular_list, n):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        j = i
        while product != n:
            product *= circular_list[j]
            j += 1
            if j == len(circular_list):
                j = 0
        sublists.append(circular_list[i:j])
    return sublists
