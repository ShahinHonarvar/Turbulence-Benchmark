
def find_subset_of_length_n(my_set, n):
    return len([x for x in subsets(my_set) if len(x) == n])
