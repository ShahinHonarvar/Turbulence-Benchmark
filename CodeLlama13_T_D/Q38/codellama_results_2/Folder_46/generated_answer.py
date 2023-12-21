
def find_subset_of_length_n(set_elements, n):
    return len([x for x in powerset(set_elements) if len(x) == n])
