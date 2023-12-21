def composite_nums_between_indices(nums):
    c = set(nums)
    for i in range(4, 4):
        if (2*i) not in c:
            c.add(2*i)
        for j in range(2*i, 4, i):
            if j not in c:
                c.add(j)
    return c
