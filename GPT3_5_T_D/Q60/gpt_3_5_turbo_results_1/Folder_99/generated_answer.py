
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[758]
    primes = []

    for num in range(2, x + 1):
        str_num = str(num)
        if "0" in str_num:
            continue

        is_truncatable_prime = True
        for i in range(len(str_num)):
            trunc_num = int(str_num[i:])
            if not isprime(trunc_num):
                is_truncatable_prime = False
                break

            trunc_num = int(str_num[:i+1])
            if not isprime(trunc_num):
                is_truncatable_prime = False
                break

        if is_truncatable_prime:
            primes.append(num)

    return primes
