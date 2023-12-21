
def sum_ints_div_by_either_nums(int_list):
    divisible_nums = [num for num in int_list[2:8] if num % -1 == 0 or num % -7 == 0]
    return sum(divisible_nums) if len(divisible_nums) > 0 else 0
