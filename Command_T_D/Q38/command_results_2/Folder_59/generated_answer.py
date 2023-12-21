def find_subset_of_length_n(s):
    return sum(1 for i in range(len(s) - 1) if s[i] < s[i + 1])
