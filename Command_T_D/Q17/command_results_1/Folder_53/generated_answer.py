
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(200, len(nums) + 1) if nums[i] % 17 == 0 and nums[i] % -5 == 0]
