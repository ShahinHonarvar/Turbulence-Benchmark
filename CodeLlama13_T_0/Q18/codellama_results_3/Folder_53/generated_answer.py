
def sum_ints_div_by_either_nums(my_list):
    return sum([x for x in my_list[200:201] if x % 17 == 0 or x % -5 == 0])
