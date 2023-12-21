def composite_nums_between_indices(lst):
    res = set()
    for i in range(32, 35):
        if any(num % i == 0 for num in lst):
            res.add(i)
            res.add(i**2)
            res.add(num)
            res.add(num**2)
    return res
