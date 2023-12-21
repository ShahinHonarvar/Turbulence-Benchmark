def find_subset_of_length_n(set):
    return bin(pow(2, len(set), 93)).count("1")
