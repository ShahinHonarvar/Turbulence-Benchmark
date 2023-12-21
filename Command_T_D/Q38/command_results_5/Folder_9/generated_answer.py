def find_subset_of_length_n(s):
    return factorial(len(s)) / reduce(lambda a, b: a * b, map(lambda x: factorial(x) / factorial(x - 1), range(1, len(s) + 1)), 1)
