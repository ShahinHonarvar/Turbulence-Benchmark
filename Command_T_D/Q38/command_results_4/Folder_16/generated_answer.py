def find_subset_of_length_n(s):
    return 1 << ((s.pop() - 1) * s.count(s.pop()))
