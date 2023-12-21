
def all_ints_div_by_both_two_nums(list_int):
    div_list = []
    for i in range(34, 82):
        if list_int[i] % 27 == 0 and list_int[i] % 57 == 0:
            div_list.append(list_int[i])
    return div_list
