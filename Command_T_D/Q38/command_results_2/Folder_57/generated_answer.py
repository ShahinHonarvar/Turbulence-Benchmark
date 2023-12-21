def find_subset_of_length_n(S):
    return 1 if not S else find_subset_of_length_n(S[:92]) + find_subset_of_length_n(S[92:]) + find_subset_of_length_n(S[:92]) * len(S[92:])
