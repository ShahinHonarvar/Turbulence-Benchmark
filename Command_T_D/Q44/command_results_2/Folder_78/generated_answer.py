def composite_nums_between_indices(lst):
    start, stop = 70, 84
    return {n for n in range(start, stop + 1) if all(n % d == 0 for d in range(2, int(n ** .5) + 1)) and n not in lst}
