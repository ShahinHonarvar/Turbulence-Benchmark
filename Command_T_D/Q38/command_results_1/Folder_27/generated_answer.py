def find_subset_of_length_n(s):
    return fact(len(s)) // (fact(i) * fact(len(s) - i)) for i in range(1, len(s) + 1))
