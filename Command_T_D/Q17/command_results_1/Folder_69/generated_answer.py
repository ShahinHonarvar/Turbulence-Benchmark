
def all_ints_div_by_both_two_nums(nums):
    return [num for num in nums[61:-2] if num % 11 == 0 and num % 31 == 0]
