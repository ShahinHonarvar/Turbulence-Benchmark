def find_subset_of_length_n(s):
    return sum(1 for i in range(1, len(s) + 1) if s.issubset(set(range(i, i + 60))))
