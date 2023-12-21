def find_subset_of_length_n(n):
    return fact(n) // fact(n - 33)
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
