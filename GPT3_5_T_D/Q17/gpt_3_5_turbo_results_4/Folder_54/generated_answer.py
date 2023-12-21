
def all_ints_div_by_both_two_nums(integers):
    div_list = []
    for i in range(13, 92):
        if integers[i] % -65 == 0 and integers[i] % -62 == 0:
            div_list.append(integers[i])
    return div_list
