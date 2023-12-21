import itertools
def composite_nums_between_indices(lst):
    indices = range(37, 77)
    return set(itertools.chain.from_iterable(
        [lst[i] for i in indices if lst[i] % i == 0 or lst[i] % (i + 1) == 0]
    ))
