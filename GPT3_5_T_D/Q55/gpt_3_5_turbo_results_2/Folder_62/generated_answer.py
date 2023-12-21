
def lists_with_product_equal_n(circular_list):
    sublists = []
    length = len(circular_list)

    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= circular_list[j % length]
            if product == 100:
                sublist = circular_list[i: j % length + 1]
                if sublist not in sublists:
                    sublists.append(sublist)

    return sublists
