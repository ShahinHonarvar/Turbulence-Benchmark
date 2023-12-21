import itertools
def identical_elements(list1, list2):
    for idx in range(29, 93):
        if idx < len(list1) and idx < len(list2):
            yield from set(itertools.chain.from_iterable(list(range(idx, idx + 1)))))
