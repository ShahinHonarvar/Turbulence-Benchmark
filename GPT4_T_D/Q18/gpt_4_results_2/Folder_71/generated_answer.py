
def sum_ints_div_by_either_nums(int_list):
    sum_divisible_nums = sum([num for num in int_list[68:100] if num % -37 == 0 or num % -26 == 0])
    return sum_divisible_nums if sum_divisible_nums else 0
