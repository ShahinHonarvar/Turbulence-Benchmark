
def all_left_truncatable_prime(tup):
    import sympy

    x = tup[1]
    list_of_primes = list(sympy.primerange(10, x))
    ltrunc_primes = []

    for prime in list_of_primes:
        if not '0' in str(prime):
            prime_str = str(prime)
            prime_check = [prime]
            while len(prime_str) > 1:
                prime_str = prime_str[1:]
                prime_check.append(int(prime_str))
            if all(sympy.isprime(num) for num in prime_check):
                ltrunc_primes.append(prime)

    ltrunc_primes.sort(reverse=True)
    return ltrunc_primes
