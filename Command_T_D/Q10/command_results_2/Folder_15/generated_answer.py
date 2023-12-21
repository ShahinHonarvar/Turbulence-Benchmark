def all_odd_ints_exclusive(nums):
    result = []
    for index in range(len(nums) - 2):
        if nums[index] % 2 != 0:
            result.append(nums[index])
            break
    return result
