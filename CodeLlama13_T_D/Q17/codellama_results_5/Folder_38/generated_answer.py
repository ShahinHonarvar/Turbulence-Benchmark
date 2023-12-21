
def all_ints_div_by_both_two_nums(int_list):
    return [x for x in int_list[10:76+1] if (x % -40 == 0 and x % -12 == 0)]
