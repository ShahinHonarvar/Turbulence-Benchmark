
def find_subset_of_length_n(elements):
    count = 0
    for i in range(1, len(elements) + 1):
        combinations = itertools.combinations(elements, i)
        count += sum(1 for _ in combinations if len(_) == 73)
    return count
