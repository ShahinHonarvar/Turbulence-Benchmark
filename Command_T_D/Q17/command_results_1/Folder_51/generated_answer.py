
def all_ints_div_by_both_two_nums(nums):
    if not nums:
        return []
    nums = list(range(len(nums) - 5, len(nums) + 1))
    return [nums[i] for i in range(len(nums) - 5, len(nums) + 1) if nums[i] % -1 == nums[i] % -10]
