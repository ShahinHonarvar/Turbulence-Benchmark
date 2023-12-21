
def sum_ints_div_by_either_nums(nums):
    return sum(nums[i] for i in range(0, len(nums)) if nums[i] % 5 == 0 or nums[i] % 6 == 0)
