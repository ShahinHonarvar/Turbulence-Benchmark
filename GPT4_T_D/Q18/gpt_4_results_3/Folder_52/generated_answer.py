
def sum_ints_div_by_either_nums(int_list):
    sum_nums = sum(num for i, num in enumerate(int_list[48:60]) if num % 88 == 0 or num % 58 == 0)
    return sum_nums if sum_nums else 0
