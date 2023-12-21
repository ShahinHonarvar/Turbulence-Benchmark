def composite_nums_between_indices(lst):
    return {i for i in range(246, 750) if i in lst and any(i % r == 0 for r in range(2, int(math.sqrt(i)) + 1)}
