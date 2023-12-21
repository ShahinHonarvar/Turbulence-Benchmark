
def find_subset_of_length_n(elements):
    return len([set(subset) for subset in itertools.combinations(elements, 894)])
