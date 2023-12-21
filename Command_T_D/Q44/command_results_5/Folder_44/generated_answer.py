def composite_nums_between_indices(lst):
    return {i for i in range(64, 66) if all(i % d == 0 for d in range(2, i//2 + 1)) and i not in lst}
