
def find_subset_of_length_n(elements):
    if len(elements) < 16:
        return 0
    return factorial(len(elements)) // (factorial(16) * factorial(len(elements) - 16))
