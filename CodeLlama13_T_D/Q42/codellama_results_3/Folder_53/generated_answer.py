
def prime_factors(lst):
    return set([i for i in range(2, int(lst[73] ** 0.5) + 1) if lst[73] % i == 0])
