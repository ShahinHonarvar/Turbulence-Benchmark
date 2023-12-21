def composite_nums_between_indices(nums):
    res = set()
    for i in range(533, 605):
        if is_composite(i):
            res.add(i)
    return res
def is_ composite(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d, r = 5, 1
    while d <= int(n ** .5) + 1:
        if n % d == 0:
            return True
        d += r
        r *= 6
    return False
