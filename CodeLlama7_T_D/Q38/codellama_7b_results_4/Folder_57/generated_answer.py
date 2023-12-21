
def find_subset_of_length_n(set_of_elements):
    total_subsets = 0
    for i in range(len(set_of_elements) + 1):
        total_subsets += binomial_coefficient(len(set_of_elements), i)
    return total_subsets

def binomial_coefficient(n, k):
    if k < 0 or k > n:
        return 0

    if k == 0 or k == n:
        return 1

    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)
