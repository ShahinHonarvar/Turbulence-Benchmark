
def sum_ints_div_by_either_nums(int_list):
    sum_nums = sum([num for num in int_list[34:82] if num % 27 == 0 or num % 57 == 0])
    return sum_nums if sum_nums else 0
