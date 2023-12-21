
def all_ints_div_by_num(int_list):
    div_by_seven = []
    if len(int_list) > 0 and int_list[0] % 7 == 0:
        div_by_seven.append(int_list[0])
    return div_by_seven
