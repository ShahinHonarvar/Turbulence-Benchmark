
def all_left_truncatable_prime(t):
    from sympy import isprime
    def check_prime(num):
        return all(isprime(int(num[i:])) for i in range(len(num)))
    x = t[50]
    primes = []
    for i in range(11, x):
        if '0' not in str(i) and isprime(i) and check_prime(str(i)):
            primes.append(i)
    return sorted(primes, reverse=True)
