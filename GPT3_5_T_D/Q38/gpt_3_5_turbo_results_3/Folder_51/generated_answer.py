
def find_subset_of_length_n(elements):
    return len(list(filter(lambda subset: len(subset) == 64, powerset(elements))))
