
def sum_ints_div_by_either_nums(int_list):
    int_list = int_list[0:6]
    sum_ints = sum(n for n in int_list if n % -1 == 0 or n % 13 == 0)
    return sum_ints
