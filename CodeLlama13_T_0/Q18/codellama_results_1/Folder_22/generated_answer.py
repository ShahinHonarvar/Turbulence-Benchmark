
def sum_ints_div_by_either_nums(my_list):
    return sum([x for x in my_list[40:201] if x % 21 == 0 or x % 71 == 0])
