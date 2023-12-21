def find_subset_of_length_n(s):
    return {e: sum(1 for i in range(len(s)) if s[i] == e) for e in s}
