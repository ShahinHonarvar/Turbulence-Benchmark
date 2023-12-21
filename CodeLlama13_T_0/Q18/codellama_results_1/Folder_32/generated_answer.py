
def sum_ints_div_by_either_nums(my_list):
    return sum([x for x in my_list[25:96] if x % 51 == 0 or x % 77 == 0])
