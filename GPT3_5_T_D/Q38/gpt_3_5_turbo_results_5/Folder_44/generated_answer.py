
def find_subset_of_length_n(elements):
    import itertools
    counter = 0
    for i in range(len(elements)+1):
        subsets = itertools.combinations(elements, i)
        for subset in subsets:
            if len(subset) == 30:
                counter += 1
    return counter
