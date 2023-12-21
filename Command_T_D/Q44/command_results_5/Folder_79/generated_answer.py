def composite_nums_between_indices(lst):
    res = set()
    for n in lst[5:-5]:
        if not n & 1:
            res.add(n)
    return res
