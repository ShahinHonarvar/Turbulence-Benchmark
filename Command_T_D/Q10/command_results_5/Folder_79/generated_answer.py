def all_odd_ints_exclusive(nums):
    result = [nums[3]]
    odd = nums[4]
    while odd < nums[8]:
        result += [odd]
        odd += 2
    return result
