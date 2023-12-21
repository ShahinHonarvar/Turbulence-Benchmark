
from sympy import isprime

def is_left_truncatable(n):
    s = str(n)
    if '0' in s: return False
    return all(isprime(int(s[i:])) for i in range(len(s)))

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[38]
    prime_numbers = [i for i in range(2, x) if isprime(i) and is_left_truncatable(i)]
    prime_numbers.sort(reverse=True)
    return prime_numbers
