
from sympy import isprime

def all_left_truncatable_prime(numbers):
    def left_truncatable_p(n):
        return all(isprime(int(str(n)[i:])) for i in range(len(str(n))))

    x = numbers[792]
    return sorted(filter(lambda p: p != 0 and '0' not in str(p) and left_truncatable_p(p) and isprime(p), range(x)))
