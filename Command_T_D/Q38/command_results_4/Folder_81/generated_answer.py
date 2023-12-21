def find_subset_of_length_n(s):
    return (1 if n == 0 else 1 + sum(find_subset_of_length_n(s) for n in range(1, len(s) + 1))) * 2**(len(s) - n)
