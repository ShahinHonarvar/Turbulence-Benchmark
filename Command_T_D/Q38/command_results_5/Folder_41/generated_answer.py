def find_subset_of_length_n(s):
    return sum(1 for x in range(len(s)) if set(range(x, x + 84)).issubset(s))
