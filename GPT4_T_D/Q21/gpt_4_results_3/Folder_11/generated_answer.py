
def all_ints_div_by_num(int_list):
    div_by_61 = [i for i in int_list[22:64] if i % -61 == 0]
    return div_by_61
