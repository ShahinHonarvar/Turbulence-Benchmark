

from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[33]
    truncatable_primes = []

    for i in range(10, x + 1):
        str_i = str(i)
        if '0' not in str_i:
            prime_check = []
            for j in range(len(str_i)):
                prime_check.append(isprime(int(str_i[j:])))
                prime_check.append(isprime(int(str_i[:len(str_i) - j])))
            if all(prime_check):
                truncatable_primes.append(i)

    truncatable_primes.sort()
    return truncatable_primes
