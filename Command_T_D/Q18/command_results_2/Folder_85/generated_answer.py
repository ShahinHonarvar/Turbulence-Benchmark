
def sum_ints_div_by_either_nums(nums):
    return sum(nums[i] for i in range(1, 9) if nums[i] % 9 == 0 or nums[i] % 3 == 0)
