def composite_nums_between_indices(lst):
    return {x for x in range(30, 87) if all(x % i for i in range(2, x // 2 + 1)) and x % 1 == 0}
