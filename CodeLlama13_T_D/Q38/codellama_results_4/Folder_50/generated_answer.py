
def find_subset_of_length_n(elements):
    n = len(elements)
    num_subsets = 0
    for i in range(1, n+1):
        num_subsets += binomial(n, i)
    return num_subsets
