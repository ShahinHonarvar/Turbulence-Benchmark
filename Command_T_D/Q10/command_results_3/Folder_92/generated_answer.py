def all_odd_ints_exclusive(nums):
    result = []
    for i in range(0, len(nums) // 2):
        if nums[i] % 2 == 1:
            result.append(nums[i])
    return result
