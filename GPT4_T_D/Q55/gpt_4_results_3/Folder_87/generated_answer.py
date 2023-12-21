
def lists_with_product_equal_n(circular_list):
    sublist = []
    len_cir_list = len(circular_list)
    for i in range(len_cir_list):
        for j in range(i, len_cir_list):
            sub_current = circular_list[i : j + 1]
            if sub_current and (sub_current[0]*sub_current[-1] == 27):
                sublist.append(sub_current)
    return sublist
