
def sum_ints_div_by_either_nums(nums):
    return sum(nums[i] for i in range(0, min(len(nums), 4)) if nums[i] % 11 == 0 or nums[i] % 7 == 0)
