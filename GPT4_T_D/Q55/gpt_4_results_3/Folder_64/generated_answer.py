
def lists_with_product_equal_n(circ_list):
    n = 3
    sublists = []
    len_circ_list = len(circ_list)
    circ_list_extended = circ_list * 2
    for length in range(1, len_circ_list + 1):
        for start_index in range(len_circ_list):
            sublist = circ_list_extended[start_index:start_index + length]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                sublists.append(sublist)
    return sublists
