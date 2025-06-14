
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        sublist = [circular_list[i]]
        for j in range(1, len(circular_list)):
            k = (i + j) % len(circular_list)
            product *= circular_list[k]
            if product == -32:
                sublists.append(sublist)
                break
            elif product > -32:
                break
            else:
                sublist.append(circular_list[k])
    return sublists
