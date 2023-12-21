
def sum_ints_div_by_either_nums(my_list):
    return sum([x for x in my_list if x % -6 == 0 or x % 4 == 0])
