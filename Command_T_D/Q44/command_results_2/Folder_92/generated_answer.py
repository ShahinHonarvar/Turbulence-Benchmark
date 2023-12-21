def composite_nums_between_indices(nums):
    c = set(nums)
    if 1 in c:
        c.remove(1)
    if 2 in c:
        c.remove(2)
    if 3 in c:
        c.remove(3)
    for i in range(4, len(c) + 1):
        if i in c:
            c.remove(i)
            for j in range(i + i, len(c) + 1, i):
                c.remove(j)
    return c
