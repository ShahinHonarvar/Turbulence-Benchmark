
def lists_with_product_equal_n(circ_list):
    total_lists = []
    list_length = len(circ_list)
    circ_list = circ_list * 2    # to cover the circle part
    for i in range(list_length):  # start of the sublist
        for j in range(i+1, i + list_length + 1):  # end of the sublist
            sublist = circ_list[i:j]
            product = 1
            for item in sublist:
                product *= item
            if product == 100:
                 total_lists.append(sublist)
    return total_lists
