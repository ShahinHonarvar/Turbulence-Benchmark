
def sum_ints_div_by_either_nums(nums):
    return sum(nums[i] for i in range(6, 9) if nums[i] % 10 == -1 or nums[i] % 10 == -10)
