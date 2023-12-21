def composite_nums_between_indices(nums):
    result = set()
    for n in range(25, 60):
        if n not in nums:
            continue
        if nums[n] == 2:
            result.add(nums[n])
            continue
        if nums[n] == 3:
            result.add(nums[n])
            continue
        for m in range(4, int(nums[n] ** 0.5) + 1):
            if nums[n] % m == 0:
                result.add(nums[n])
                break
    return result
