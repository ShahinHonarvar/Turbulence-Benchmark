
def find_subset_of_length_n(elements):
    import itertools
    count = 0
    for r in range(1, len(elements)+1):
        for subset in itertools.combinations(elements, r):
            if len(subset) == 45:
                count += 1
    return count
