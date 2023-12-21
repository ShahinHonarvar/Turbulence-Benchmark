
def sum_ints_div_by_either_nums(my_list):
    return sum([i for i in my_list[60:201] if i % 9 == 0 or i % 11 == 0])
