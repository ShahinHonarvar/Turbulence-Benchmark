
def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(240, 902):
        if nums[i] % 546 == 0 or nums[i] % 709 == 0:
            sum += nums[i]
    return sum
