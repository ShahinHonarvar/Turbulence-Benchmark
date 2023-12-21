def find_subset_of_length_n(s):
    return sum(a == n for a, b in enumerate(s) if b == n)
