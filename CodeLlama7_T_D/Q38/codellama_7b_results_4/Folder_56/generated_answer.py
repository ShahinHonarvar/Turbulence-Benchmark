
def find_subset_of_length_n(my_set):
    num_subsets = 0
    for i in range(1, len(my_set) + 1):
        num_subsets += binomial_coefficient(len(my_set), i))
    return num_subsets

def binomial_coefficient(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return factorial(n) // (factorial(k) * factorial(n - k)))

def factorial(n):

    result = 1

    for i in range(2, n + 1)):
        result *= i

    return result
