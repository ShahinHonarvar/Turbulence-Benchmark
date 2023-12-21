def all_odd_ints_inclusive(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            result.append(nums[i])
    return result
