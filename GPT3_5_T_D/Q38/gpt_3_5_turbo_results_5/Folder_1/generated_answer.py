
def find_subset_of_length_n(elements):
    n = 85
    if n > len(elements):
        return 0
    return factorial(len(elements)) // (factorial(n) * factorial(len(elements) - n))
