
import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = []

    for i in range(10, x + 1):
        is_truncatable_prime = True
        str_i = str(i)

        if '0' in str_i or not sympy.isprime(i):
            continue

        for j in range(1, len(str_i)):
            if not (sympy.isprime(int(str_i[j:])) and sympy.isprime(int(str_i[:-j]))):
                is_truncatable_prime = False
                break

        if is_truncatable_prime:
            primes.append(i)

    return sorted(primes, reverse=True)
