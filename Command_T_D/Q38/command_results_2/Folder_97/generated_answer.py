def find_subset_of_length_n(s):
    return sum(1 for x in range(len(s)) if not s[x])
