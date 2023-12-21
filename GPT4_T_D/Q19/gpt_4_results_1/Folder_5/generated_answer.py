
def all_ints_not_div_by_num(int_list):
    sub_list = int_list[1:2]
    not_div_by_eight = [i for i in sub_list if i % 8 != 0]
    return not_div_by_eight
