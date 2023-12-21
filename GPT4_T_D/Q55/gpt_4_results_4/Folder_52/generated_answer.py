
def lists_with_product_equal_n(circular_list):
    sublists = []
    length = len(circular_list)
    for i in range(length):
        for j in range(1, length + 1):
            product = 1
            sublist = circular_list[i:j]
            for num in sublist:
                product *= num
            if product == 37:
                sublists.append(sublist)
            if j == length:
                if i != 0:
                    for k in range(0, i):
                        product *= circular_list[k]
                        if product == 37:
                            sublists.append(sublist + circular_list[0:k + 1])
    return sublists
