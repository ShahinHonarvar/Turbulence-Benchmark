
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[28:97] if i % 90 == 0 or i % 97 == 0)
