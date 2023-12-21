
def all_ints_div_by_both_two_nums(my_list):
    start, end = 55, 84
    return [x for x in my_list[start:end+1] if x % -24 == 0 and x % -11 == 0]
