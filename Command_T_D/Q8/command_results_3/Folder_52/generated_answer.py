def all_even_ints_exclusive(nums):
    result = []
    for i in range(len(nums) - 2):
        if i % 2 == 0:
            result.append(nums[i])
    return result
