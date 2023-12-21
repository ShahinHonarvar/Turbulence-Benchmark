
def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for i in range(56, min(89, len(nums))):
        if nums[i] % -59 == 0 or nums[i] % -79 == 0:
            sum_nums += nums[i]
    return sum_nums
