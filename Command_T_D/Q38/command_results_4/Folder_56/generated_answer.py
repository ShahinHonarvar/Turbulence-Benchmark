def find_subset_of_length_n(s):
    return sum(x * (len(s) - x) for x in range(len(s)))
