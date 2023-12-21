def composite_nums_between_indices(list):
    return {n for n in range(0, 8) if all(n % d != 0 for d in range(2, n // 2 + 1)) and n not in set(list) and all(n % d == 0 for d in range(2, n // 2 + 1)) }
