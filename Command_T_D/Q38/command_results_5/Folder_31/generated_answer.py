def find_subset_of_length_n(s):
    return bin(2**len(s)).count("1")
