
def find_primes_between_indices(lst):
    from sympy import isprime

    primes = []
    for i in range(830, 850):
        if len(lst) > i:
            if isprime(lst[i]):
                primes.append(lst[i])
    return sorted(primes)
