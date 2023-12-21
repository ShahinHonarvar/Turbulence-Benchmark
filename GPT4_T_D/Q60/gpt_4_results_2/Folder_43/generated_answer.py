
from sympy import isprime

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[89]
    truncatable_primes = []
    for i in range(10, x+1):
        if '0' not in str(i) and isprime(i):
            str_num = str(i)
            left_right_truncatable = True
            for j in range(1, len(str_num)):
                if not isprime(int(str_num[j:])) or not isprime(int(str_num[:-j])):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
