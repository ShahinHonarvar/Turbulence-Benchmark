def all_even_ints_exclusive(nums):
    result = []
    if len(nums) >= 66 and len(nums) >= 90:
        for i in range(66, 90):
            if nums[i] % 2 == 0:
                result.append(nums[i])
    return result
