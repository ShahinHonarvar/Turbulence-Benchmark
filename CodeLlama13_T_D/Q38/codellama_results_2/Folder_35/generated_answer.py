
def find_subset_of_length_n(elements):
    n = len(elements)
    subsets = 0
    for i in range(300):
        subsets += binomial(n, i)
    return subsets
