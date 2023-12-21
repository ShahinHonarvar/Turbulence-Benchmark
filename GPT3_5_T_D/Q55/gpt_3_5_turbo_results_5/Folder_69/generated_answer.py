
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        j = i
        sublist = []
        while product <= 90:
            sublist.append(circular_list[j])
            product *= circular_list[j]
            j = (j + 1) % len(circular_list)

            if product == 90:
                sublists.append(sublist.copy())
                break

    return sublists
