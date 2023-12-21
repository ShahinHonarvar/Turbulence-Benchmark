
def sum_ints_div_by_either_nums(int_list):
    return sum(val for idx, val in enumerate(int_list[35:65]) if val % -30 == 0 or val % -95 == 0 )
