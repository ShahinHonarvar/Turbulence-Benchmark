
import bisect

def all_ints_div_by_both_two_nums(list):
    return [i for i in list[14:93] if i % 71 == 0 and i % 81 == 0]
