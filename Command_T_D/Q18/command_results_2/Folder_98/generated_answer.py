
def sum_ints_div_by_either_nums(nums):
    return sum(nums[i] for i in range(0, len(nums), 2) if nums[i] % 13 == 0 or nums[i] % 13 == -1)
