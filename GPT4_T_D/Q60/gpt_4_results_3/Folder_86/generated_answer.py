
from sympy import isprime

def all_left_right_truncatable_prime(tuple_):
    x = tuple_[126]
    
    def is_left_right_truncatable(number: int) -> bool:
        if '0' in str(number):
            return False
        right = number % 10 ** (len(str(number)) - 1)
        left = number // 10
        while right > 0 and left > 0:
            if not isprime(left) or not isprime(right):
                return False
            right = right % 10 ** (len(str(right)) - 1)
            left = left // 10
        return isprime(left) or isprime(right)

    return sorted([i for i in range(10, x + 1) if isprime(i) and is_left_right_truncatable(i)], reverse=True)
