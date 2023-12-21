
from sympy import prevprime, isprime

def all_left_right_truncatable_prime(t):
    x = t[94]
    primes = []
    i = prevprime(x+1)
    while i > 10:
        str_prime = str(i)
        if '0' not in str_prime:
            for j in range(len(str_prime)):
                left = int(str_prime[j:])
                right = int(str_prime[:len(str_prime)-j])
                if not (isprime(left) and isprime(right)):
                    break
            else:
                primes.append(i)
        i = prevprime(i)
    return sorted(primes)
