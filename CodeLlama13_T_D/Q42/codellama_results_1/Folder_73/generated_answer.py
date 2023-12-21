
def prime_factors(lst):
    return set([p for i in range(len(lst)) if lst[i] == 41 and p for p in range(2, int(lst[i]**0.5) + 1) if lst[i] % p == 0])
