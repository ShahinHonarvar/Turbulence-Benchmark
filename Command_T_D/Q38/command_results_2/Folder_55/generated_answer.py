def find_subset_of_length_n(s):
    return fact(len(s)) // fact(n) * fact(n - 1) // fact(len(s) - n)
