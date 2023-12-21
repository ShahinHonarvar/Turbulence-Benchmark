def find_subset_of_length_n(s):
    return {*s} & set(range(len(s))) & set(range(len(s)-1, -1, -1))
