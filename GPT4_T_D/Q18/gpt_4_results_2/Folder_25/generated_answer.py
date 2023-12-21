
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[25:81] if i % -20 == 0 or i % -26 == 0)
