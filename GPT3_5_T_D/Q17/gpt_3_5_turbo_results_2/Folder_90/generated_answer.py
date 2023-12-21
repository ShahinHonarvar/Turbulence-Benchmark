
def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for i in range(138, 425):
        if nums[i] % -863 == 0 and nums[i] % -329 == 0:
            divisible_nums.append(nums[i])
    return divisible_nums
