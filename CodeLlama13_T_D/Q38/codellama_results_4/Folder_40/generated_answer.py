
def find_subset_of_length_n(my_set):
    return len([i for i in range(1, len(my_set)+1) if len(set(combinations(my_set, i))) == n])
