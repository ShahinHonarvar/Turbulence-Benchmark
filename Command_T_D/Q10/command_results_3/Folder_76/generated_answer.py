def all_odd_ints_exclusive(nums):
    result = []
    if (361 in nums and nums[361] % 2 == 1) and (643 in nums and nums[643] % 2 == 1):
        result = nums[361:643:2]
    return result
