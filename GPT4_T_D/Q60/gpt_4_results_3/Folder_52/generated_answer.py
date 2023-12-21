
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[52]

    def is_left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        return all(isprime(int(s[i:])) and isprime(int(s[:-i])) for i in range(len(s)))

    result = [n for n in range(10, x+1) if is_left_right_truncatable(n)]
    result.sort(reverse=True)
    return result
