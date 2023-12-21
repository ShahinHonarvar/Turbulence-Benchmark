
def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 32 or len(nums) > 99:
        return []
    return [i for i in range(32, 99) if nums[i] % -11 == 0 and nums[i] % -15 == 0]
