
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(31, 50) if nums[i] % 81 == 0 and nums[i] % 64 == 0]
