def find_subset_of_length_n(s):
    return 1 if n == 0 else find_subset_of_length_n(s) + find_subset_of_length_n(s, 1) + find_subset_of_length_n(s, 2) + find_subset_of_length_n(s, 3) + find_subset_of_length_n(s, 4) + find_subset_of_length_n(s, 5) + find_subset_of_length_n(s, 6)
