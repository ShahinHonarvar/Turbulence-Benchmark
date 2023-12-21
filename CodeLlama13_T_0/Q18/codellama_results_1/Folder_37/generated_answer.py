
def sum_ints_div_by_either_nums(my_list):
    return sum([x for x in my_list[2:8] if x % -1 == 0 or x % -7 == 0])
