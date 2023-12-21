
def find_subset_of_length_n(set_of_elements):
    number_of_all_subsets = 0
    for i in range(len(set_of_elements) + 1):
        number_of_all_subsets += binomial_coefficient(i, 6)
    return number_of_all_subsets

def binomial_coefficient(n, k):
    if n < k:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)
