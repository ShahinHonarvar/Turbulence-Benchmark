
def prime_factors(list):
    return set([i for i in range(2, 60) if all([j % i != 0 for j in list])])
