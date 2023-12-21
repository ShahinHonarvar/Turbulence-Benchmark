
def sum_ints_div_by_either_nums(int_list):
    divisible_nums = [num for num in int_list[250:630] if num % 850 == 0 or num % 587 == 0]
    return sum(divisible_nums) if divisible_nums else 0
