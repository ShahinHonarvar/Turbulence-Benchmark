
def find_subset_of_length_n(elements):
    return len([x for x in range(1, 723) if all(len(set(x)) == n for n in elements)])
