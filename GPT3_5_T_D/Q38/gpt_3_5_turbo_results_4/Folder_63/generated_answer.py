
def find_subset_of_length_n(set_of_elements):
    import itertools
    count = 0
    for subset in itertools.combinations(set_of_elements, 57):
        count += 1
    return count
