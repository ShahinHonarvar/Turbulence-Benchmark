def all_odd_ints_exclusive(nums):
    result = []
    for i in range(4, len(nums) - 1, 2):
        if nums[i] % 2:
            result.append(nums[i])
    return result
