
def prime_factors(lst):
    return set([i for i in range(2, int(lst[993]**0.5) + 1) if lst[993] % i == 0])
