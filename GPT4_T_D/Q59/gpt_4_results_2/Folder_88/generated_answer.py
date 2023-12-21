
def all_left_truncatable_prime(t):
    def isprime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(prime):
        str_prime = str(prime)
        if '0' in str_prime:
            return False
        for i in range(len(str_prime)):
            if not isprime(int(str_prime[i:])):
                return False
        return True

    x = t[93]
    primes = [i for i in range(2, x) if isprime(i)]
    left_truncatable_primes = [p for p in primes if left_truncatable(p)]

    return sorted(left_truncatable_primes)
