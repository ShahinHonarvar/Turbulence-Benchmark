
def all_ints_div_by_both_two_nums(int_list, low_index=34, high_index=81):
    return [x for x in int_list[low_index:high_index+1] if x % 27 == 0 and x % 57 == 0]
