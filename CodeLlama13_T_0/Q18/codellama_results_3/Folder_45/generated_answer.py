
def sum_ints_div_by_either_nums(my_list):
    return sum([x for x in my_list[30:201] if x % -115 == 0 or x % 115 == 0])
