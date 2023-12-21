
def prime_factors(list_of_integers):
    return set([i for i in range(2, 31) if all(j % i == 0 for j in list_of_integers)])
