def find_subset_of_length_n(s):
    return {k: v for k, v in sorted(s.items(), key=lambda x: x[1])}
