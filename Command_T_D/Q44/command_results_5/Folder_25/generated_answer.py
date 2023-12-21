import set
def composite_nums_between_indices(nums):
    c = set()
    for x in range(75, 95):
        if not x in c:
            for i in range(x**2, x**2 + x):
                if not i in c:
                    c.add(i)
    return c
