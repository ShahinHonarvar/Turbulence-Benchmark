
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[73]
    primes = []
    for i in range(10, x+1):
        if '0' in str(i): continue
        str_i = str(i)
        length = len(str_i)
        primes.append(i)
        for j in range(1, length):
            if not isprime(int(str_i[j:])) or not isprime(int(str_i[:length-j])):
                primes.remove(i)
                break
    primes = sorted([p for p in primes if isprime(p)], reverse=True)
    return primes
