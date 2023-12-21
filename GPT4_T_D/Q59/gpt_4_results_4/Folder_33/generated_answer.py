
from sympy import isprime

def all_left_truncatable_prime(numbers): 
    x = numbers[945]
    resulting_primes = []

    for num in range(11, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        found = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                found = False
                break
        if found:
            resulting_primes.append(num)

    resulting_primes.sort(reverse=True)

    return resulting_primes
