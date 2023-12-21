def find_subset_of_length_n(s):
    return {*s} | {*{a for a in s if s.count(a) == 6}}
