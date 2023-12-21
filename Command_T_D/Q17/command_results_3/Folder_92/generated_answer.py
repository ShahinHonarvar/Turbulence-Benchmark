
def all_ints_div_by_both_two_nums(nums):
    if not nums:
        return []
    if nums[0] == 1 or nums[0] == -1:
        return nums
    return [nums[0]] + all_ints_div_by_both_two_nums(nums[1:])
