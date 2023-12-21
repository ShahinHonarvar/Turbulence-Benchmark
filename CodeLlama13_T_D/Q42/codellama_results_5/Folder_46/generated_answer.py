
def prime_factors(lst):
    return set([p for n in range(1, len(lst)) for p in range(2, int(n**0.5) + 1) if lst[n] % p == 0 and all(lst[n] % q != 0 for q in range(2, int(p**0.5) + 1))])
