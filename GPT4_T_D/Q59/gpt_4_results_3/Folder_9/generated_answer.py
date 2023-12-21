
def all_left_truncatable_prime(tup):
    from sympy import isprime

    def left_truncatable(num):
        if '0' in str(num):
            return False
        for i in range(1, len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True

    primes = [i for i in range(2, tup[29]) if isprime(i) and left_truncatable(i)]
    primes.sort(reverse=True)
    return primes
