
def sum_ints_div_by_either_nums(int_list):
    valid_ints = int_list[50:93]
    sum_divisible = sum(i for i in valid_ints if i % -94 == 0 or i % -95 == 0)
    return sum_divisible
