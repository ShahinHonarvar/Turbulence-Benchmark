def composite_nums_between_indices(lst):
    res = set()
    for n in range(43, 86 + 1):
        if n not in lst:
            continue
        if all(n % d == 0 for d in range(2, int(n ** .5) + 1)):
            res.add(n)
    return res
