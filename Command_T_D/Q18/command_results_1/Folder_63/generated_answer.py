
def sum_ints_div_by_either_nums(nums):
    return sum(nums[i] for i in range(31, 50) if nums[i] % 81 == 0 or nums[i] % 64 == 0)
