
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(10, 100):
        if i % 10 == 0 or i % 100 == 0:
            result += nums[i]
    return result
