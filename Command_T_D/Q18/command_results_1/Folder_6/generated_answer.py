
def sum_ints_div_by_either_nums(nums):
    return sum(nums[i] for i in range(41, 57) if nums[i] % 82 == 0 or nums[i] % 90 == 0)
