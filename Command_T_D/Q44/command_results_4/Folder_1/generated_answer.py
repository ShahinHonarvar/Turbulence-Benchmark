def composite_nums_between_indices(list):
    return {n for n in list if n >= 69 and n <= 83 and all(x % n == 0 for x in range(1, int(n ** .5) + 1)) }
