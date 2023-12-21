
def all_left_truncatable_prime(tup):
    import itertools
    from sympy import isprime

    x = tup[97]
    all_primes = [i for i in itertools.chain.from_iterable((str(i) for i in range(1, 10)) for _ in range(1, len(str(x)))) if isprime(int(i)) and '0' not in i]
    filter_primes = [int(i) for i in all_primes if all(isprime(int(i[j:])) for j in range(len(i)))]

    filter_primes.sort(reverse=True)
    return [i for i in filter_primes if i<x]
