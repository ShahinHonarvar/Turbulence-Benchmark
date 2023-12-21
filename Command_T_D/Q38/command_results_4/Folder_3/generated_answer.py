def find_subset_of_length_n(s):
    return fact(s.count(1)) * inv_fact(s.count(1))
