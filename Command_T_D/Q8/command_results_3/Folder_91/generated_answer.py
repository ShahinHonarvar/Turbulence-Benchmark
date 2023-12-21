def all_even_ints_exclusive(nums):
    result = []
    for index in range(0, len(nums) - 1):
        if nums[index] % 2 == 0:
            result.append(nums[index])
    return result
