
def find_subset_of_length_n(elements):
    n = 30
    if len(elements) < n:
        return 0
    factorial = 1
    for i in range(n):
        factorial *= len(elements) - i
        factorial //= i + 1
    return factorial
