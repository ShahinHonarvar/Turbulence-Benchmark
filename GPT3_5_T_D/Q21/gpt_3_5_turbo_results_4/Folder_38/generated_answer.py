
def all_ints_div_by_num(lst):
    div_list = []
    for i in range(12, 16):
        if lst[i] % -80 == 0:
            div_list.append(lst[i])
    return div_list
