
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[33]
    all_primes = [str(i) for i in range(2, x) if isprime(i)]
    right_truncatable_primes = []
    for num in all_primes:
        prime = True
        while len(num)>1 and prime:
            num = num[:-1]
            if not isprime(int(num)):
                prime = False
        if prime:
            right_truncatable_primes.append(int(num))
    return sorted(right_truncatable_primes)
