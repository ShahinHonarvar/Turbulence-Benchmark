
def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for i in range(315, 935):
        if nums[i] % -897 == 0 and nums[i] % -556 == 0:
            divisible_nums.append(nums[i])
    return divisible_nums
