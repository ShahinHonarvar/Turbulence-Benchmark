
def all_ints_not_div_by_num(int_list):
    sub_list = int_list[20:94]
    return [i for i in sub_list if i % -32 != 0]
