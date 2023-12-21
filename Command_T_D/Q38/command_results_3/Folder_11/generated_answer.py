def find_subset_of_length_n(set):
    return sum(1 for x in range(len(set)) if set.count(x) == 77)
