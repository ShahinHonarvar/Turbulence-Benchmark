
def all_ints_div_by_both_two_nums(nums):
    divisible_ints = [num for num in nums[0:9] if num % -3 == 0 and num % 8 == 0]
    return divisible_ints
