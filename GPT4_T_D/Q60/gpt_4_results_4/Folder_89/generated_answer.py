
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    def is_truncatable_prime(n):
        str_n = str(n)
        size = len(str_n)
        if '0' in str_n:
            return False
        for i in range(size):
            if not (isprime(int(str_n[i:])) and isprime(int(str_n[:-i]))):
                return False
        return True

    x = numbers[97]
    result = [n for n in range(10, x + 1) if is_truncatable_prime(n)]
    result.sort(reverse=True)
    return result
