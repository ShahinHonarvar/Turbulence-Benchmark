def all_odd_ints_inclusive(nums):
    result = []
    for i in range(3, len(nums) - 2, 2):
        if nums[i] % 2 == 1:
            result.append(nums[i])
    return result
