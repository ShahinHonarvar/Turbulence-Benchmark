import set
def composite_nums_between_indices(nums):
    c = set(nums)
    for i in range(29, 93):
        if i in c:
            c |= set(range(2, i//2 + 1))
            c |= set(range(i**2, i**2 + i, i))
    return c
