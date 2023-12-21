
def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for i in range(34, 82):
        if nums[i] % 27 == 0 and nums[i] % 57 == 0:
            divisible_nums.append(nums[i])
    return divisible_nums
