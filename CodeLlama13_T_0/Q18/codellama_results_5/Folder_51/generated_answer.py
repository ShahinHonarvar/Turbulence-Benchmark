
def sum_ints_div_by_either_nums(my_list):
    return sum([x for x in my_list[6:10] if x % -1 == 0 or x % -10 == 0])
