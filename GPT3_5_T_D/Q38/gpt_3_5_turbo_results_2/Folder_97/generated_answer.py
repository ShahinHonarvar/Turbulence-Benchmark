
def find_subset_of_length_n(elements_set):
    n = 219
    if n > len(elements_set):
        return 0
    else:
        num_subsets = 1
        for i in range(len(elements_set), len(elements_set) - n, -1):
            num_subsets *= i
        for i in range(1, n + 1):
            num_subsets //= i
        return num_subsets
