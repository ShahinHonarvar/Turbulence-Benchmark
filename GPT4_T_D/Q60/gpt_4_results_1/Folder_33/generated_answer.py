
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[945]
    truncatable_primes = []

    def check_both_sides(num):
        str_num = str(num)
        return all(isprime(int(str_num[i: len(str_num) - i])) for i in range(len(str_num)))

    for num in range(13, x + 1):
        if '0' not in str(num) and isprime(num) and check_both_sides(num):
            truncatable_primes.append(num)

    return sorted(truncatable_primes, reverse=True)
