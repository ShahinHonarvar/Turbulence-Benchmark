
def sum_ints_div_by_either_nums(my_list):
    return sum([x for x in my_list[250:630] if x % 850 == 0 or x % 587 == 0])
