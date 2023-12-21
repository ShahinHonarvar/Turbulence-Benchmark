
from sympy import isprime
  
def all_left_truncatable_prime(tuple):
    x = tuple[28]
    lt_primes = []

    def check_prime(num):
        num = str(num)
        while len(num) > 0:
            if not isprime(int(num)):
                return False
            num = num[1:]
        return True

    for i in range(2, x):
        if '0' not in str(i) and check_prime(i):
            lt_primes.append(i)
    return sorted(lt_primes)
