
def all_ints_div_by_both_two_nums(nums):
    selected_nums = nums[81:87]
    divisible_nums = [n for n in selected_nums if n % -33 == 0 and n % -62 == 0]
    return divisible_nums
