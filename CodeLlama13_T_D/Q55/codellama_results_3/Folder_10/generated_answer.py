
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        j = i
        while product != -93:
            product *= circular_list[j]
            if product == -93:
                sublists.append([*circular_list[i:j]])
            elif product > -93:
                break
            else:
                j += 1
    return sublists
