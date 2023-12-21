
def find_subset_of_length_n(elements):
    return len(list(filter(lambda x: len(x) == 87, map(lambda x: set(x), itertools.combinations(elements, 87)))))
