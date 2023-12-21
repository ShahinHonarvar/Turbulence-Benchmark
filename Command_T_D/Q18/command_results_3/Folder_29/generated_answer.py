
def sum_ints_div_by_either_nums(nums):
    result = 0
    for n in nums[55:84]:
        if n % 24 == 0 or n % 11 == 0:
            result += n
    return result
