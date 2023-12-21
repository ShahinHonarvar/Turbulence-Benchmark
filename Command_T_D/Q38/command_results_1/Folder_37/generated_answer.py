def find_subset_of_length_n(s):
    return sum(map(lambda x: (1 if x in s else 0), range(n)))
