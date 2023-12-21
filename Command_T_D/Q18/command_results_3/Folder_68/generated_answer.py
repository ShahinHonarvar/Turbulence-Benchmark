
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(len(nums) - 6, -1, -1):
        if nums[i] % 5 == 0 or nums[i] % 7 == 0:
            result += nums[i]
            break
    return result
