def composite_nums_between_indices(lst):
    return {n for n in range(65, 67) for i in range(2, int(n**(0.5)) + 1) if n % i == 0 and n not in lst}
