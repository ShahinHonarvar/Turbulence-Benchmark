
def sum_ints_div_by_either_nums(my_list):
    return sum(i for i in my_list[0:7] if i % -5 == 0 or i % -6 == 0)
