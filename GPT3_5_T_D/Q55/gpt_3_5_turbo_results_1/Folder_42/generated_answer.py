
def lists_with_product_equal_n(circ_list):
    sublists = []
    length = len(circ_list)
    for i in range(length):
        product = 1
        for j in range(i, length+i):
            product *= circ_list[j % length]
            if product == 25:
                sublists.append(circ_list[i:j % length+1])
    return sublists
