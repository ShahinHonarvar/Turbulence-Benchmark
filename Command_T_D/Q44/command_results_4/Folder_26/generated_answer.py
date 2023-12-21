def composite_nums_between_indices(nums):
    res = set()
    for i in range(22, 50+1):
        if any(n % i == 0 for n in nums):
            res.update(range(i, i + i))
    return res
