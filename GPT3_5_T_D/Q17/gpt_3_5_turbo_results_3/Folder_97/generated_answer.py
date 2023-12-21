
def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for i in range(58, 76):
        if nums[i] % 72 == 0 and nums[i] % 62 == 0:
            divisible_nums.append(nums[i])
    return divisible_nums
