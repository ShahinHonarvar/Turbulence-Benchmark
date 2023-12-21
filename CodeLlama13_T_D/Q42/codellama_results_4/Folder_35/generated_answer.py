
def prime_factors(lst):
    return set(filter(lambda x: x in lst[993], list(range(2, int(sqrt(lst[993])) + 1)) if lst[993] % x == 0 else None for x in range(2, int(sqrt(lst[993]) + 1))))
