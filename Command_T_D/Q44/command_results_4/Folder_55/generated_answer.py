def composite_nums_between_indices(nums):
    res = set()
    for i in range(10, 100):
        if nums[i] % i != 0:
            continue
        j = nums[i] // i
        while j > 1:
            res.add(nums[i])
            i += 1
            j //= i
    return res
