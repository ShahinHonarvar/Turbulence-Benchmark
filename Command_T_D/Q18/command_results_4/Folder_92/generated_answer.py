
def sum_ints_div_by_either_nums(nums):
    result = nums[0] if nums[0] % 2 == 0 else 0
    for i in range(1, len(nums)):
        result += nums[i] if nums[i] % 2 == 0 else 0
    return result
