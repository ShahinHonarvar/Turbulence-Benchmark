
def sum_ints_div_by_either_nums(int_list):
    list_subset = int_list[13:77]
    divisible_nums = [num for num in list_subset if num % -66 == 0 or num % -32 == 0]
    return sum(divisible_nums) if divisible_nums else 0
