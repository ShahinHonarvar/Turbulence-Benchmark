def find_subset_of_length_n(s):
    return {el for sub in set(s) for el in range(len(sub), len(s), len(sub) + 1)}
