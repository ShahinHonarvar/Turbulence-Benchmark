
def find_subset_of_length_n(elements):
    return len([sub for i in range(len(elements)) for sub in itertools.combinations(elements, i) if len(sub) == n])
