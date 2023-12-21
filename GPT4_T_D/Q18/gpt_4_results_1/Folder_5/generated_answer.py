
def sum_ints_div_by_either_nums(num_list):
    return sum(i for i in num_list[0:2] if i % 4 == 0 or i % -6 == 0)
