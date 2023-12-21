
def sum_ints_div_by_either_nums(int_list):
    if len(int_list) == 0:
        return 0
    else:
        return int_list[0] if int_list[0] % 1 == 0 or int_list[0] % -1 == 0 else 0
