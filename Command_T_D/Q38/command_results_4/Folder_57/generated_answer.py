def find_subset_of_length_n(set):
    return {*set} | {set} | set(set) | set(set) | set(set)
