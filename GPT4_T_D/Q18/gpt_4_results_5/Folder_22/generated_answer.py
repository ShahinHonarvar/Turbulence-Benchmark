
def sum_ints_div_by_either_nums(nums):
    sum_of_nums = 0
    for i in range(40, min(len(nums),201)):
        if nums[i] % 21 == 0 or nums[i] % 71 == 0:
            sum_of_nums += nums[i]
    return sum_of_nums
