
def all_right_truncatable_prime(tup):
    from sympy import isprime

    x = tup[54]

    def check_right_truncatable(n):
        n = str(n)
        return all(isprime(int(n[i:])) for i in range(len(n)))

    def get_right_truncatable_primes(x):
        return [i for i in range(x) if check_right_truncatable(i)]

    right_truncatable_primes = get_right_truncatable_primes(x)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
