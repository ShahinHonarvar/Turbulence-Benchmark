
def find_subset_of_length_n(elements):
    return sum(1 for i in range(1, len(elements)+1) for subset in itertools.combinations(elements, i))
