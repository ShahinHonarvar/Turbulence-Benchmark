def find_subset_of_length_n(s):
    return 1 if len(s) == 1 else 1 + sum(
        find_subset_of_length_n(s[:i]) + find_subset_of_length_n(s[:i] + s[i+1:])
        for i in range(1, len(s))
    )
