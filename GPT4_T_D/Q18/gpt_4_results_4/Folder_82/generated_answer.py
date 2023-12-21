
def sum_ints_div_by_either_nums(int_list):
    sublist = int_list[20:201]
    divisible_nums = [num for num in sublist if num % -20 == 0 or num % -200 == 0]
    return sum(divisible_nums) if divisible_nums else 0
