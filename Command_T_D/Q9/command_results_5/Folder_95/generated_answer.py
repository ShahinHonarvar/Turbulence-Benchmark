def all_odd_ints_inclusive(nums):
    result = []
    for i in range(min(len(nums) - 1, 82), min(len(nums) - 1, 86) + 1):
        if nums[i] % 2 == 1:
            result.append(nums[i])
    return result
