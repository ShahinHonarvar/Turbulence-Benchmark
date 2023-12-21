
def all_ints_not_div_by_num(int_list):
    sub_list = int_list[267:586]
    result = [x for x in sub_list if x % 840 != 0]
    return result
