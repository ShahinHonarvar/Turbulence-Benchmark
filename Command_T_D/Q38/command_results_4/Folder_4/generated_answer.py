def find_subset_of_length_n(n):
    return math.factorial(len(n)) // math.factorial(len(n)-15) // math.factorial(15)
