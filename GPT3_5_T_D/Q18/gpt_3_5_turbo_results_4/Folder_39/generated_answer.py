
def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(13, 77):
        if nums[i] % -66 == 0 or nums[i] % -32 == 0:
            sum += nums[i]
    return sum
