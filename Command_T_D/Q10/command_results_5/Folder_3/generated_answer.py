def all_odd_ints_exclusive(nums):
    result = []
    if nums:
        for i in range(len(nums) - 2):
            if nums[i] % 2 == 1:
                result.append(nums[i])
                if nums[i] == 93:
                    break
        if len(result) == 0:
            result.append(0)
    return result
