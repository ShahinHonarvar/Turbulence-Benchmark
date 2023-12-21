def all_even_ints_exclusive(nums):
    result = []
    for i in range(0, len(nums)-1):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    if nums[len(nums)-1] % 2 == 0:
        result.append(nums[len(nums)-1])
    return result
