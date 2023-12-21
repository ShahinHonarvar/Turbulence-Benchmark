
def find_subset_of_length_n(elements):
    n = 534
    factorial_n = 1
    factorial_n_minus_i = 1
    for i in range(1, n + 1):
        factorial_n *= i
        factorial_n_minus_i *= (n - i + 1)
    count = factorial_n_minus_i // factorial_n
    return count
