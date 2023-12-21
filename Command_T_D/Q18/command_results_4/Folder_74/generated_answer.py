
def sum_ints_div_by_either_nums(nums):
    return sum(nums[90:97] if (nums[i] % 13 == 0 or nums[i] % 35 == 0) else 0 for i in range(len(nums)))
