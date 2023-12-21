
def find_subset_of_length_n(element_set):
    n = 33
    if len(element_set) < n:
        return 0
    elif len(element_set) == n:
        return 1
    else:
        return factorial(len(element_set)) // (factorial(n) * factorial(len(element_set) - n))
