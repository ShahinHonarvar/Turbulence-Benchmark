
def sum_ints_div_by_either_nums(int_list):
    subset_list = int_list[30:201]
    divisible_nums = [num for num in subset_list if num % 115 == 0 or num % -115 == 0]
    return sum(divisible_nums) if divisible_nums else 0
