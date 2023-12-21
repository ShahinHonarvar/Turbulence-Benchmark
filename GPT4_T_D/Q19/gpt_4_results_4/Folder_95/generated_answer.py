
def all_ints_not_div_by_num(int_list):
    range_list = int_list[39:52]
    result_list = [i for i in range_list if i % -41 != 0]
    return result_list
