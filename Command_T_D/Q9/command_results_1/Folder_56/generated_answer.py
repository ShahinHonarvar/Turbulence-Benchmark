def all_odd_ints_inclusive(nums):
    result = []
    for i in range(0, len(nums) - 1):
        if nums[i] % 2 == 1:
            result.append(nums[i])
    if nums[len(nums) - 1] % 2 == 1:
        result.append(nums[len(nums) - 1])
    return result
