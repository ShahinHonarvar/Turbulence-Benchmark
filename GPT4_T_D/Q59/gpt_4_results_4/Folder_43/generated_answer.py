
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[89]
    all_primes = []
    for i in range(10,x):
        if isprime(i) and '0' not in str(i):
            string_i = str(i)
            flag = True
            while len(string_i)>1:
                string_i = string_i[1:]
                if not isprime(int(string_i)):
                    flag = False
                    break
            if flag:
                all_primes.append(i)
    return sorted(all_primes, reverse=True)
