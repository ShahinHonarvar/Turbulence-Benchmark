
def sum_ints_div_by_either_nums(num_list):
    divisible_nums = [num for num in num_list[86:91] if num % -71 == 0 or num % -67 == 0]
    return sum(divisible_nums) if divisible_nums else 0
