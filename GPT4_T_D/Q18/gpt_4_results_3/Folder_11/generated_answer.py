
def sum_ints_div_by_either_nums(int_list):
    sum_divisible = sum([num for num in int_list[22:25] if num % -85 == 0 or num % -30 == 0])
    return sum_divisible if sum_divisible else 0
