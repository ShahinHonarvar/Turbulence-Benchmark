
def all_ints_div_by_num(int_list):
    div_list = []
    for i in range(10, 38):
        if int_list[i] % -64 == 0:
            div_list.append(int_list[i])
    return div_list
