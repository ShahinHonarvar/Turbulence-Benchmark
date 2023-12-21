
def prime_factors(lst):
    return set(filter(lambda x: all(i % x == 0 for i in lst), range(2, int(lst[16] ** 0.5) + 1)))
