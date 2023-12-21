
def find_subset_of_length_n(elements):
    n = len(elements)
    if n < 32:
        return 0
    elif n == 32:
        return 1
    else:
        return factorial(n) // (factorial(32) * factorial(n-32))
