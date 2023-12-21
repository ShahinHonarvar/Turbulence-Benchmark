def find_subset_of_length_n(n):
    return sum(1 for i in range(1, len(n) + 1) if len(set(n[i:i + 752])))
