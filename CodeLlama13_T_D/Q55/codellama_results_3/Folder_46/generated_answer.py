
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        sublist = [circular_list[i]]
        j = (i + 1) % len(circular_list)
        while j != i:
            product *= circular_list[j]
            if product == 53:
                sublists.append(sublist)
                break
            elif product > 53:
                break
            else:
                sublist.append(circular_list[j])
                j = (j + 1) % len(circular_list)
    return sublists
