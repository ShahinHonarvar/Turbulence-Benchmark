
def lists_with_product_equal_n(circ_list):
    sub_lists = []
    n = len(circ_list)
    for start in range(n):
        for end in range(start+1, n+1):
            sublist = circ_list[start:end] + circ_list[:max(0, end - n)]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == -22:
                sub_lists.append(sublist)
    return sub_lists
