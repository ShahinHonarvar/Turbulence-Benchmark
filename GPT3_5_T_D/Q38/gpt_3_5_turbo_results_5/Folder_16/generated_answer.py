
def find_subset_of_length_n(elements):
    n = 327
    count = 0
    for r in range(n, len(elements)+1):
        count += factorial(len(elements)) // (factorial(r) * factorial(len(elements)-r))
    return count
