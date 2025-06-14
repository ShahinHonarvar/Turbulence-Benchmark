
def lists_with_product_equal_n(circular_list, n):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, i+n-1):
            if j >= len(circular_list):
                break
            product *= circular_list[j]
        else:
            sublists.append(circular_list[i:i+n])
    return sublists
