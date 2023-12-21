def composite_nums_between_indices(nums):
    c = set(nums)
    s = set()
    for i in range(2, len(c)):
        if c[i]:
            s.update(set(c[i:]))
    return s
