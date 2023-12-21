
def lists_with_product_equal_n(circular_list, n):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        sublist = [circular_list[i]]
        for j in range(1, len(sublist)):
            product *= circular_list[(i + j) % len(circular_list)]
            if product == n:
                sublists.append(sublist)
                break
            elif product > n:
                break
            else:
                sublist.append(circular_list[(i + j) % len(circular_list)])
    return sublists
