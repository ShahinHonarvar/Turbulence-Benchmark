
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[4]
    primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue

        prime_status = []
        for i in range(len(str_num)):
            if isprime(int(str_num[i:])):
                prime_status.append(True)
            else:
                prime_status.append(False)

        if all(prime_status):
            primes.append(num)
    return sorted(primes)
