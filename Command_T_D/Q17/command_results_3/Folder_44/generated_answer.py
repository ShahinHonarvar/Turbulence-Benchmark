
def all_ints_div_by_both_two_nums(nums):
    if 25 <= len(nums) <= 70:
        return [nums[i] for i in range(25, len(nums) - 1) if nums[i] % 74 == 0 and nums[i] % 15 == 0]
    else:
        return []
