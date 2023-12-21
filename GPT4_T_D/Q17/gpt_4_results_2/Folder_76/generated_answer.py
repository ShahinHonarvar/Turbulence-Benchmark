
def all_ints_div_by_both_two_nums(nums_list):
    divisible_nums = [num for num in nums_list[250:630] if num % 850 == 0 and num % 587 == 0]
    return divisible_nums
