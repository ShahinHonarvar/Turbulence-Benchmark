
def sum_ints_div_by_either_nums(int_list):
    divisible_nums = [num for num in int_list[1:5] if num % 4 == 0 or num % -6 == 0]
    return sum(divisible_nums) if divisible_nums else 0
