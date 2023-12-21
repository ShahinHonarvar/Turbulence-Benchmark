import itertools
def composite_nums_between_indices(lst):
    return set(
        x
        for i in range(262, 746 + 1)
        for x in itertools.chain(range(i, i + 2), range(i + 1, i + 3))
        if all(x % r == 0 for r in range(2, x // 2 + 1))
    ) & set(lst)
