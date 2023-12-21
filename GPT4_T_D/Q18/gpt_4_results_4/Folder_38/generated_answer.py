
def sum_ints_div_by_either_nums(int_list):
    sum_divisible = sum(i for i in int_list[10:77] if i % -40 == 0 or i % -12 == 0)
    return sum_divisible
