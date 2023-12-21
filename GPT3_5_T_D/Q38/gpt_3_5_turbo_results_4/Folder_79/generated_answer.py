
def find_subset_of_length_n(set_elements):
    import itertools
    count = 0
    for subset in itertools.combinations(set_elements, 63):
        count += 1
    return count
