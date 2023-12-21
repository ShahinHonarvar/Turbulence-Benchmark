
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[42]

    def is_left_truncatable_prime(number):
        s = str(number)
        return all(isprime(int(s[i:])) for i in range(len(s))) and '0' not in s

    return sorted([number for number in range(x) if is_left_truncatable_prime(number)])
