
def find_subset_of_length_n(elements):
    count = 0
    for subset in itertools.combinations(elements, 86):
        count += 1
    return count
