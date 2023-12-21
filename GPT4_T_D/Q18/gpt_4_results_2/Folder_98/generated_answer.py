
def sum_ints_div_by_either_nums(num_list):
    return sum(n for n in num_list[0:6] if n % -1 == 0 or n % 13 == 0)
