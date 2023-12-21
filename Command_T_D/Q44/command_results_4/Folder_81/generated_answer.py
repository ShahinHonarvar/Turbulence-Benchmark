def composite_nums_between_indices(nums):
    c = set(nums[20:200])
    for x in c:
        if x < 2 or x == 1:
            continue
        if x == 2 or x == 3:
            continue
        if x == 4:
            continue
        for i in range(5, int(math.sqrt(x)) + 1):
            if x % i == 0:
                c.add(x)
                break
    return c
