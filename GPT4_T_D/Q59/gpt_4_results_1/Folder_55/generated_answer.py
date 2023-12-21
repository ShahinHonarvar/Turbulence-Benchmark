
from sympy import isprime

def all_left_truncatable_prime(tup):
    num = tup[73]
    primes = []

    def check_truncatable(num):
        num = str(num)
        for i in range(len(num)):
            if not isprime(int(num[i:])):
                return False
        return True

    for i in range(10, num):
        if '0' not in str(i) and isprime(i) and check_truncatable(i):
            primes.append(i)

    return sorted(primes, reverse=True)
