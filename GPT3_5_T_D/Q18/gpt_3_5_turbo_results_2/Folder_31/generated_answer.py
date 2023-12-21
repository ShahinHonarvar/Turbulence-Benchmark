
def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(56, 89):
        if nums[i] % -59 == 0 or nums[i] % -79 == 0:
            sum += nums[i]
    return sum
