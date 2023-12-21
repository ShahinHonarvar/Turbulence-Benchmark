def all_odd_ints_inclusive(nums):
    result = []
    for i in range(10, len(nums) + 10):
        if nums[i] % 2 == 1:
            result.append(nums[i])
    return result
