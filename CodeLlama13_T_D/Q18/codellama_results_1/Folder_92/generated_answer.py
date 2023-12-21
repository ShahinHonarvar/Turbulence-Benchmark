
def sum_ints_div_by_either_nums(my_list):
    return sum(i for i in my_list if (i % 1) == 0 or (i % -1) == 0)
