
def find_subset_of_length_n(elements):
    return len(set(filter(lambda x: len(x) == 180, powerset(elements))))
