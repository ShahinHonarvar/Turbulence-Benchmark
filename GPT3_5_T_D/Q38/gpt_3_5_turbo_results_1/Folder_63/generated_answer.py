
def find_subset_of_length_n(elements):
    counter = 0
    for subset in itertools.combinations(elements, 57):
        counter += 1
    return counter
