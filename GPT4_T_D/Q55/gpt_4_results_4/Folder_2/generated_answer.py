
def lists_with_product_equal_n(circ_list):
    circ_list = circ_list + circ_list
    length = len(circ_list) // 2
    sublists = []
    for i in range(length):
        for j in range(i + 1, length + i + 1):
            sublist = circ_list[i:j]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == -968:
                sublists.append(sublist)
    return sublists
