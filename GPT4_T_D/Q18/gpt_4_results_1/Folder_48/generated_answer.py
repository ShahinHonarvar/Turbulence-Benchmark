
def sum_ints_div_by_either_nums(int_list):
    sub_list = int_list[306:958]
    divisible_nums = [num for num in sub_list if num % 982 == 0 or num % 319 == 0]
    return sum(divisible_nums) if divisible_nums else 0
