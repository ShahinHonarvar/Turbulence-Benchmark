
def all_ints_div_by_both_two_nums(my_list):
    return [x for x in my_list if x % -3 == 0 and x % 8 == 0][:9]
