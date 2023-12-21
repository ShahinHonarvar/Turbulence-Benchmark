
def sum_ints_div_by_either_nums(my_list):
    return sum([i for i in my_list[0:9] if i % -3 == 0 or i % 8 == 0])
