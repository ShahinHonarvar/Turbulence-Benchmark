
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(len(circular_list)):
            index = (i + j) % len(circular_list)
            product *= circular_list[index]
            if product == 46:
                sublist = circular_list[i:index+1]
                sublists.append(sublist)
    return sublists
