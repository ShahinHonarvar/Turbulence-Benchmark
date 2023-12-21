def sum_odd_ints_inclusive(nums):
    result = 0
    for i in range(0, len(nums) - 1):
        if nums[i] % 2 == 0:
            result += nums[i]
        elif nums[i] == 1:
            result += 1
    if nums[len(nums) - 1] % 2 == 1:
        result += nums[len(nums) - 1]
    return result
